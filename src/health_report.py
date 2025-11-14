# src/monthly_health_report.py
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Set

import matplotlib
matplotlib.use("Agg")  # safe for headless environments (CI)
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).parent.parent
REPO_INFO = ROOT / "files" / "repo_info.json"
HISTORY_JSON = ROOT / "reports" / "monthly_health_history.json"
MONTHLY_MD = ROOT / "reports" / "monthly_health_report.md"

# Plot output files
HEALTH_PNG = ROOT / "reports" / "health_status_over_time.png"
TESTED_PNG = ROOT / "reports" / "tested_vs_never_tested.png"
OPEN_ISSUES_PNG = ROOT / "reports" / "open_issues_over_time.png"
ADDED_PNG = ROOT / "reports" / "added_models_per_month.png"

# Health classification thresholds (can be tuned later)
HEALTH_RECENT_DAYS = 60   # days since last test to be considered "recent"
OUTDATED_DAYS = 180       # days since last test to be considered "outdated"

# Corporate color palette
PALETTE = [
    "#50285A",  # primary purple
    "#FAD782",  # yellow
    "#FAA08B",  # orange
    "#DC9FDC",
    "#AA96FA",
    "#8DC7FA",
    "#BEE6B4",
    "#D2D2D2",
]


# -----------------------------
# Data loading / saving
# -----------------------------
def _load_repo_info() -> List[Dict[str, Any]]:
    """
    Load repository metadata from repo_info.json.

    Returns:
        List[Dict[str, Any]]: Repository entries.
    """
    if not REPO_INFO.exists():
        return []
    return json.loads(REPO_INFO.read_text(encoding="utf-8"))


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
    previous_repos: Set[str],
) -> List[Dict[str, Any]]:
    """
    Detect models that were added since the previous snapshot.

    Args:
        data: Current repository info.
        previous_repos: Repositories present in the last snapshot.

    Returns:
        A list of "added model" summaries (repository_name + slug).
    """
    added: List[Dict[str, Any]] = []
    for r in data:
        repo_name = r.get("repository_name")
        if not repo_name or repo_name in previous_repos:
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

    Produces:
        - health_status_over_time.png
        - tested_vs_never_tested.png
        - open_issues_over_time.png
        - added_models_per_month.png
    """
    if not history:
        # Nothing to plot yet
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

    # 1) Health stacked bar plot
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.bar(x, healthy, color=PALETTE[0], label="Healthy")
    ax.bar(x, failing, bottom=healthy, color=PALETTE[1], label="Failing")
    bottom_outdated = [healthy[i] + failing[i] for i in range(len(x))]
    ax.bar(x, outdated, bottom=bottom_outdated, color=PALETTE[2], label="Outdated")
    ax.set_xticks(x)
    ax.set_xticklabels(months, rotation=45, ha="right")
    ax.set_ylabel("Number of models")
    ax.set_title("Model health over time")
    ax.legend()
    fig.tight_layout()
    fig.savefig(HEALTH_PNG, dpi=150)
    plt.close(fig)

    # 2) Tested vs never tested stacked bar
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.bar(x, tested, color=PALETTE[3], label="Tested at least once")
    ax.bar(x, never_tested, bottom=tested, color=PALETTE[4], label="Never tested")
    ax.set_xticks(x)
    ax.set_xticklabels(months, rotation=45, ha="right")
    ax.set_ylabel("Number of models")
    ax.set_title("Tested vs never tested")
    ax.legend()
    fig.tight_layout()
    fig.savefig(TESTED_PNG, dpi=150)
    plt.close(fig)

    # 3) Open issues line chart
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(x, with_open_issues, marker="o", color=PALETTE[5], label="Models with open issues")
    ax.set_xticks(x)
    ax.set_xticklabels(months, rotation=45, ha="right")
    ax.set_ylabel("Models with open issues")
    ax.set_title("Models with open issues over time")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OPEN_ISSUES_PNG, dpi=150)
    plt.close(fig)

    # 4) Added models per month bar chart
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.bar(x, added_counts, color=PALETTE[6], label="Added models")
    ax.set_xticks(x)
    ax.set_xticklabels(months, rotation=45, ha="right")
    ax.set_ylabel("Models added")
    ax.set_title("New models added per month")
    ax.legend()
    fig.tight_layout()
    fig.savefig(ADDED_PNG, dpi=150)
    plt.close(fig)


# -----------------------------
# Markdown builder
# -----------------------------
def _build_monthly_markdown(
    month_id: str,
    snapshot: Dict[str, Any],
    history: List[Dict[str, Any]],
) -> str:
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
        "## 📈 Global trends over time",
        "",
        "### 🩺 Health status (Healthy / Failing / Outdated)",
        "",
        "![Health status over time](./health_status_over_time.png)",
        "",
        "### 🧪 Tested vs never tested",
        "",
        "![Tested vs never tested](./tested_vs_never_tested.png)",
        "",
        "### ❗ Models with open issues",
        "",
        "![Models with open issues](./open_issues_over_time.png)",
        "",
        "### 🆕 Models added per month",
        "",
        "![New models added per month](./added_models_per_month.png)",
        "",
        "## 🔢 Snapshot for this month",
        "",
        "\n".join(summary_lines),
        "",
        "## 🆕 Models added this month",
        "",
        added_table,
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
    data = _load_repo_info()
    history = _load_history()

    month_id = _get_current_month_id()
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if history:
        previous_repos = set(history[-1].get("all_repositories", []))
    else:
        previous_repos = set()

    totals = _compute_stats(data)
    all_repos = _get_all_repo_names(data)
    added_models = _detect_added_models(data, previous_repos)

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

    _save_history(history)

    # Generate plots based on full history (including this month)
    _build_trend_plots(history)

    # Build and write markdown report
    _ensure_reports_dir()
    md = _build_monthly_markdown(month_id, snapshot, history)
    MONTHLY_MD.write_text(md, encoding="utf-8")

    print(f"Monthly health report generated for {month_id}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
