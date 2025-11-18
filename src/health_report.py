# src/monthly_health_report.py
from __future__ import annotations

import json
import numpy as np
from collections import Counter 
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Set

import matplotlib
matplotlib.use("Agg")  
import matplotlib.pyplot as plt  

from ersilia_maintenance.config import (
    PALETTE,
    HEALTH_RECENT_DAYS,
    OUTDATED_DAYS,
    ROOT_DIR,
    REPO_INFO_PATH,
)

HISTORY_JSON = ROOT_DIR / "reports" / "monthly_health_history.json"
MONTHLY_MD = ROOT_DIR / "reports" / "monthly_health_report.md"

# Plot output files (grouped figures)
HEALTH_TESTED_PNG = ROOT_DIR / "reports" / "health_and_testing.png"
ISSUES_ADDED_PNG = ROOT_DIR / "reports" / "issues_and_added.png"
DISTRIBUTIONS_PNG = ROOT_DIR / "reports" / "distributions_tasks_source.png"

# -----------------------------
# Data loading / saving
# -----------------------------
def _load_repo_info() -> List[Dict[str, Any]]:
    """
    Load repository metadata from repo_info.json.

    Returns:
        List[Dict[str, Any]]: Repository entries.
    """
    if not REPO_INFO_PATH.exists():
        return []
    return json.loads(REPO_INFO_PATH.read_text(encoding="utf-8"))


def _load_history() -> List[Dict[str, Any]]:
    """
    Load the monthly health history JSON file if it exists.

    Returns:
        List[Dict[str, Any]]: List of monthly snapshots.
    """
    if not HISTORY_JSON.exists():
        return []
    return json.loads(HISTORY_JSON.read_text(encoding="utf-8"))


def _save_history(history: List[Dict[str, Any]]) -> None:
    """
    Save the monthly health history JSON file.

    Args:
        history: The list of monthly snapshots to persist.
    """
    HISTORY_JSON.parent.mkdir(parents=True, exist_ok=True)
    HISTORY_JSON.write_text(json.dumps(history, indent=2), encoding="utf-8")

def _filter_finalized_models(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filter out models that are still in progress / not finalized.

    We exclude entries whose 'status' indicates a work-in-progress model,
    so they don't affect health stats or plots.

    Treated as "in progress" if status is (case-insensitive):
      - "in progress"
      - "in_progress"
      - "draft"
    """
    filtered: List[Dict[str, Any]] = []
    for r in data:
        status = str(r.get("status", "")).strip().lower()
        if status == "in progress":
            continue
        filtered.append(r)
    return filtered


# -----------------------------
# Date / health helpers
# -----------------------------
def _parse_iso_date(value: Any) -> datetime | None:
    """
    Parse an ISO-8601 date string into a datetime object in UTC.

    Args:
        value: The ISO-8601 formatted string (e.g. "2025-01-01T12:00:00Z").

    Returns:
        A timezone-aware datetime in UTC, or None if invalid.
    """
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def _days_since(date_str: Any) -> int | None:
    """
    Compute the number of days elapsed since the given ISO-8601 date.

    Args:
        date_str: The ISO-8601 formatted string.

    Returns:
        Number of days since that date, or None if the date is invalid.
    """
    dt = _parse_iso_date(date_str)
    if dt is None:
        return None
    delta = datetime.now(timezone.utc) - dt
    return delta.days


def _classify_health(entry: Dict[str, Any]) -> str:
    """
    Classify model health as 'healthy', 'failing', or 'outdated'.

    Rules:
        - failing: open_issues > 0
        - outdated: last_test_date missing or older than OUTDATED_DAYS
        - healthy: last_test_date within HEALTH_RECENT_DAYS and no open issues
        - otherwise: 'outdated' (conservative)

    Args:
        entry: Repository metadata entry.

    Returns:
        Health label: 'healthy', 'failing', or 'outdated'.
    """
    open_issues = entry.get("open_issues") or 0
    try:
        oi = int(open_issues)
    except (TypeError, ValueError):
        oi = 0

    days_since_test = _days_since(entry.get("last_test_date"))

    if oi > 0:
        return "failing"

    if days_since_test is None or days_since_test > OUTDATED_DAYS:
        return "outdated"

    if days_since_test <= HEALTH_RECENT_DAYS:
        return "healthy"

    return "outdated"


def _compute_stats(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Compute aggregate statistics for the current snapshot.

    Args:
        data: Repository metadata entries.

    Returns:
        Dictionary with global totals and health buckets.
    """
    total = len(data)
    with_open_issues = 0
    never_tested = 0
    health_counts = {"healthy": 0, "failing": 0, "outdated": 0}

    for r in data:
        open_issues = r.get("open_issues") or 0
        try:
            oi = int(open_issues)
        except (TypeError, ValueError):
            oi = 0

        if oi > 0:
            with_open_issues += 1

        if not r.get("last_test_date"):
            never_tested += 1

        label = _classify_health(r)
        if label in health_counts:
            health_counts[label] += 1

    no_open_issues = total - with_open_issues
    tested_at_least_once = total - never_tested

    return {
        "total_models": total,
        "with_open_issues": with_open_issues,
        "no_open_issues": no_open_issues,
        "tested_at_least_once": tested_at_least_once,
        "never_tested": never_tested,
        "healthy": health_counts["healthy"],
        "failing": health_counts["failing"],
        "outdated": health_counts["outdated"],
    }


def _get_current_month_id() -> str:
    """
    Get the current month identifier in YYYY-MM format.

    Returns:
        Month string.
    """
    return datetime.now(timezone.utc).strftime("%Y-%m")


def _get_all_repo_names(data: List[Dict[str, Any]]) -> Set[str]:
    """
    Collect all repository names from the metadata entries.

    Args:
        data: Repository metadata.

    Returns:
        Set of repository_name strings.
    """
    names: Set[str] = set()
    for r in data:
        name = r.get("repository_name")
        if name:
            names.add(str(name))
    return names


def _detect_added_models(
    data: List[Dict[str, Any]],
    month_id: str, ) -> List[Dict[str, Any]]:
    """
    Detect models that were (packaged) in the given month.

    A model is considered "added" in a month if its 'last_packaging_date'
    falls within that calendar month (based on the current snapshot in
    repo_info.json).

    Args:
        data: Current repository info (already filtered, e.g. no in-progress).
        month_id: Target month in 'YYYY-MM' format (e.g. '2025-10').

    Returns:
        A list of "added model" summaries (repository_name + slug).
    """
    added: List[Dict[str, Any]] = []
    for r in data:
        repo_name = r.get("repository_name")
        if not repo_name:
            continue

        lp = r.get("last_packaging_date")
        if not lp:
            continue

        try:
            # last_packaging_date is 'YYYY-MM-DD'
            dt = datetime.fromisoformat(str(lp))
        except ValueError:
            # If the format is weird, skip this entry
            continue

        if dt.strftime("%Y-%m") != month_id:
            continue

        added.append(
            {
                "repository_name": repo_name,
                "slug": r.get("slug"),
            }
        )
    return added


# -----------------------------
# Plot generation
# -----------------------------
def _ensure_reports_dir() -> None:
    """Ensure the reports directory exists."""
    MONTHLY_MD.parent.mkdir(parents=True, exist_ok=True)


def _build_trend_plots(history: List[Dict[str, Any]]) -> None:
    """
    Generate PNG plots for the main trends based on monthly history.

    Produces two grouped figures:
        - health_and_testing.png  (health over time + tested vs never tested)
        - issues_and_added.png    (models with open issues + added per month)
    """
    if not history:
        return

    snapshots = sorted(history, key=lambda s: s.get("month", ""))
    months = [s.get("month", "—") for s in snapshots]
    totals_list = [s.get("totals", {}) for s in snapshots]

    healthy = [t.get("healthy", 0) for t in totals_list]
    failing = [t.get("failing", 0) for t in totals_list]
    outdated = [t.get("outdated", 0) for t in totals_list]

    tested = [t.get("tested_at_least_once", 0) for t in totals_list]
    never_tested = [t.get("never_tested", 0) for t in totals_list]

    with_open_issues = [t.get("with_open_issues", 0) for t in totals_list]
    added_counts = [len(s.get("added_models", [])) for s in snapshots]

    x = list(range(len(months)))
    _ensure_reports_dir()

    # ------------------------------------------------------------------
    # Figure 1: Health + testing (restyled)
    # ------------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(
        1,
        2,
        figsize=(12, 4.5),
        sharex=True,
        constrained_layout=False,
    )

    # Bar width (dynamic)
    n_months = max(1, len(months))
    if n_months <= 2:
        bar_width = 0.2
    elif n_months <= 4:
        bar_width = 0.35
    else:
        bar_width = 0.55

    # Cleaner axes style
    for ax in (ax1, ax2):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#AAAAAA")
        ax.spines["bottom"].set_color("#AAAAAA")
        ax.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.4)
        ax.set_axisbelow(True)

    # ───────────────────────
    # Health stacked bar plot
    # ───────────────────────
    bottom_failing = healthy
    bottom_outdated = [healthy[i] + failing[i] for i in range(len(x))]

    ax1.bar(x, healthy, width=bar_width, color=PALETTE[0], edgecolor="none", label="Healthy")
    ax1.bar(x, failing, width=bar_width, bottom=bottom_failing, color=PALETTE[1],
            edgecolor="none", label="Failing")
    ax1.bar(x, outdated, width=bar_width, bottom=bottom_outdated, color=PALETTE[2],
            edgecolor="none", label="Outdated")

    ax1.set_title("Model health over time", fontsize=12)
    ax1.set_ylabel("Number of models")
    ax1.set_xticks(x)
    ax1.set_xticklabels(months, rotation=45, ha="right", fontsize=9)

    # Legend just below the axes (tidy spacing)
    ax1.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.25),
        ncol=3,
        frameon=False,
        fontsize=10,
    )

    # ───────────────────────
    # Test coverage plot
    # ───────────────────────
    ax2.bar(x, tested, width=bar_width, color=PALETTE[3], edgecolor="none",
            label="Tested at least once")
    ax2.bar(x, never_tested, width=bar_width, bottom=tested, color=PALETTE[4],
            edgecolor="none", label="Never tested")

    ax2.set_title("Test coverage over time", fontsize=12)
    ax2.set_xticks(x)
    ax2.set_xticklabels(months, rotation=45, ha="right", fontsize=9)

    ax2.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.25),
        ncol=2,
        frameon=False,
        fontsize=10,
    )

    # Main title, move up slightly
    fig.suptitle("Health & testing overview", fontsize=13, y=0.97)

    # Reduce bottom whitespace (previously too big)
    fig.tight_layout()
    fig.savefig(HEALTH_TESTED_PNG, dpi=150)
    plt.close(fig)

    # -------------------------
    # Figure 2: Issues + added
    # -------------------------
    fig, (ax3, ax4) = plt.subplots(
        1,
        2,
        figsize=(12, 4),
        sharex=True,
        constrained_layout=True,
    )

    # Open issues line chart
    ax3.plot(
        x,
        with_open_issues,
        marker="o",
        linewidth=2.0,
        color=PALETTE[5],
        label="Models with open issues",
    )
    ax3.set_title("Models with open issues")
    ax3.set_ylabel("Number of models")
    ax3.set_xticks(x)
    ax3.set_xticklabels(months, rotation=45, ha="right")
    ax3.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)
    ax3.legend(frameon=False)

    # Added models per month
    ax4.bar(x, added_counts, color=PALETTE[6], label="New models")
    ax4.set_title("New models added per month")
    ax4.set_xticks(x)
    ax4.set_xticklabels(months, rotation=45, ha="right")
    ax4.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.5)


    fig.suptitle("Issues & growth", fontsize=13, y=1.02)
    fig.savefig(ISSUES_ADDED_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _add_smart_labels(ax, wedges, labels, sizes, small_thresh=5.0):
    """
    Attach labels to wedges, placing labels inside large slices and outside
    with callouts for very small slices.
    """
    total = sum(sizes)

    for w, label, size in zip(wedges, labels, sizes):
        pct = (size / total) * 100
        ang = (w.theta2 + w.theta1) / 2.0
        x = np.cos(np.deg2rad(ang))
        y = np.sin(np.deg2rad(ang))

        # Decide text color based on wedge face color
        face = w.get_facecolor()  # RGBA
        r, g, b = face[:3]
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        inside_color = "white" if luminance < 0.5 else "black"

        if pct >= small_thresh:
            ax.text(
                x * 0.55,
                y * 0.55,
                f"{pct:.1f}%",
                ha="center",
                va="center",
                fontsize=9,
                color=inside_color
            )
        else:
            ax.text(
                x * 1.15,
                y * 1.15,
                f"({pct:.1f}%)",
                ha="center",
                va="center",
                fontsize=9,
                color=inside_color
            )
            ax.plot([x * 0.8, x * 1.05], [y * 0.8, y * 1.05], color="gray", lw=0.8)

def _build_distributions_figure(data: List[Dict[str, Any]]) -> None:
    """
    Build a single figure with two pie charts:

      - Left:  source_type distribution
      - Right: subtask distribution (with rare subtasks grouped into 'Other')

    Both pies include legends and smart label placement for tiny slices.
    """
    if not data:
        return

    # ----------- Source type counts -----------
    source_counter: Counter[str] = Counter()
    for r in data:
        src = r.get("source_type") or "Unknown"
        source_counter[str(src)] += 1

    source_labels = list(source_counter.keys()) or ["No data"]
    source_sizes = list(source_counter.values()) or [1]

    # ----------- Subtask counts -----------
    task_counter: Counter[str] = Counter()
    for r in data:
        task = r.get("subtask") or "Unknown"
        task_counter[str(task)] += 1

    if not task_counter:
        task_labels = ["No data"]
        task_sizes = [1]
    else:
        items = sorted(task_counter.items(), key=lambda kv: kv[1], reverse=True)
        max_slices = 7
        main_items = items[:max_slices]
        other_items = items[max_slices:]

        task_labels = [name for name, _ in main_items]
        task_sizes = [count for _, count in main_items]

        if other_items:
            task_labels.append("Other")
            task_sizes.append(sum(count for _, count in other_items))

    # ----------- Colors -----------
    def _colors_for(n: int) -> List[str]:
        return [PALETTE[i % len(PALETTE)] for i in range(n)]

    source_colors = _colors_for(len(source_labels))
    task_colors = _colors_for(len(task_labels))

    # ----------- Build figure -----------
    _ensure_reports_dir()
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(13, 6))

    fig.suptitle(
        "Model distributions (current snapshot)",
        fontsize=18,
        y=0.97,
    )

    # ----------- LEFT PIE (Source Types) -----------
    wedges_l, texts_l = ax_left.pie(
        source_sizes,
        labels=None,   # we handle labels manually
        colors=source_colors,
        startangle=90,
    )
    ax_left.set_title("Source type distribution", fontsize=14)
    ax_left.axis("equal")

    _add_smart_labels(ax_left, wedges_l, source_labels, source_sizes)

    # Legend
    ax_left.legend(
        wedges_l,
        source_labels,
        title="Source types",
        loc="center left",
        bbox_to_anchor=(1.0, 0.5),
        fontsize=10,
        title_fontsize=11,
    )

    # ----------- RIGHT PIE (Subtasks) -----------
    wedges_r, texts_r = ax_right.pie(
        task_sizes,
        labels=None,
        colors=task_colors,
        startangle=90,
    )
    ax_right.set_title("Subtask distribution", fontsize=14)
    ax_right.axis("equal")

    _add_smart_labels(ax_right, wedges_r, task_labels, task_sizes)

    # Legend
    ax_right.legend(
        wedges_r,
        task_labels,
        title="Subtasks",
        loc="center left",
        bbox_to_anchor=(1.0, 0.5),
        fontsize=10,
        title_fontsize=11,
    )

    # Improve spacing
    fig.tight_layout(rect=[0.0, 0.0, 0.85, 0.90])

    fig.savefig(DISTRIBUTIONS_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)

# -----------------------------
# Markdown builder
# -----------------------------
def _build_monthly_markdown(
    month_id: str,
    snapshot: Dict[str, Any],
    history: List[Dict[str, Any]],) -> str:
    """
    Build the monthly health report markdown content, including:
      - PNG charts for the main time trends
      - Snapshot for the current month
      - Models added this month
    """
    totals = snapshot["totals"]
    added_models = snapshot["added_models"]

    summary_lines = [
        f"- 📦 **Total models:** {totals['total_models']}",
        f"- ✅ **Healthy models:** {totals['healthy']}",
        f"- 🔴 **Failing models:** {totals['failing']}",
        f"- ⏳ **Outdated models:** {totals['outdated']}",
        f"- 🧪 **Tested at least once:** {totals['tested_at_least_once']}",
        f"- 🕳️ **Never tested:** {totals['never_tested']}",
        f"- ❗ **With open issues:** {totals['with_open_issues']}",
    ]

    # Table of models added this month (no contributor columns yet)
    if added_models:
        added_header = (
            "| 🧬 Repository | 🪪 Slug |\n"
            "|---------------|---------|\n"
        )
        added_rows = [
            f"| {m.get('repository_name', '—')} | {m.get('slug', '—')} |"
            for m in added_models
        ]
        added_table = added_header + "\n".join(added_rows) + "\n"
    else:
        added_table = "_No new models were added this month._\n"

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    md_parts: List[str] = [
        "# 📊 Monthly Health Report",
        "",
        f"**Month:** {month_id}",
        f"**Generated at:** {now_utc} (UTC)",
        "",
        "## 🔢 Snapshot for this month",
        "",
        "\n".join(summary_lines),
        "",
        "## 🆕 Models packaged this month",
        "",
        added_table,

        "## 📈 Global trends over time",
        "",
        "### 🩺 Health & testing overview",
        "",
        "![Health & testing](./health_and_testing.png)",
        "",
        "### ❗ Issues & new models",
        "",
        "![Issues & added models](./issues_and_added.png)",
        "",
        "### 🧩 Task & source type distributions (current snapshot)",
        "",
        "![Distributions](./distributions_tasks_source.png)",
        ""
    ]


    return "\n".join(md_parts) + "\n"


# -----------------------------
# Main
# -----------------------------
def main() -> int:
    """
    Generate the monthly health report and update the history JSON.

    Steps:
        - Load repo_info.json
        - Load existing monthly history
        - Compute current-month snapshot
        - Detect added models compared to previous month
        - Append or update snapshot in history
        - Save history and write monthly markdown report
        - Generate PNG plots for time trends
    """
    raw_data = _load_repo_info()
    # Exclude models that are still in progress
    data = _filter_finalized_models(raw_data)

    history = _load_history()

    month_id = _get_current_month_id()
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    totals = _compute_stats(data)
    all_repos = _get_all_repo_names(data)

    # Added models for *this* month, based on last_packaging_date
    added_models = _detect_added_models(data, month_id)

    snapshot = {
        "month": month_id,
        "generated_at": now_iso,
        "totals": totals,
        "added_models": added_models,
        "all_repositories": sorted(all_repos),
    }

    # Append or replace snapshot for this month
    if history and history[-1].get("month") == month_id:
        history[-1] = snapshot
    else:
        history.append(snapshot)

    
    data = _filter_finalized_models(raw_data)

    _save_history(history)

        # Generate plots based on full history (including this month)
    _build_trend_plots(history)

    # Generate grouped distributions figure (source type + subtask)
    _build_distributions_figure(data)

    # Build and write markdown report
    _ensure_reports_dir()
    md = _build_monthly_markdown(month_id, snapshot, history)
    MONTHLY_MD.write_text(md, encoding="utf-8")

    print(f"Monthly health report generated for {month_id}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
