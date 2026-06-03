# src/health_report.py
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Dict, List, Set

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ersilia_maintenance.config import (
    OUTDATED_DAYS,
    ROOT_DIR,
    REPO_INFO_PATH,
    PALETTE,
)

HISTORY_JSON = ROOT_DIR / "reports" / "monthly_health_history.json"
MONTHLY_MD = ROOT_DIR / "reports" / "monthly_health_report.md"

HEALTH_TESTED_PNG = ROOT_DIR / "reports" / "health_and_testing.png"
ISSUES_ADDED_PNG = ROOT_DIR / "reports" / "issues_and_added.png"
DISTRIBUTIONS_PNG = ROOT_DIR / "reports" / "distributions_tasks_source.png"

# Indices into PALETTE for the three health buckets
COL_PASSING    = 6  # light green  #BEE6B4
COL_NOT_TESTED = 1  # yellow       #FAD782
COL_FAILING    = 2  # salmon       #FAA08B


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------

def _load_repo_info() -> List[Dict[str, Any]]:
    if not REPO_INFO_PATH.exists():
        return []
    return json.loads(REPO_INFO_PATH.read_text(encoding="utf-8"))


def _load_history() -> List[Dict[str, Any]]:
    if not HISTORY_JSON.exists():
        return []
    return json.loads(HISTORY_JSON.read_text(encoding="utf-8"))


def _save_history(history: List[Dict[str, Any]]) -> None:
    HISTORY_JSON.parent.mkdir(parents=True, exist_ok=True)
    HISTORY_JSON.write_text(json.dumps(history, indent=2), encoding="utf-8")


def _ensure_reports_dir() -> None:
    MONTHLY_MD.parent.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Filtering
# ---------------------------------------------------------------------------

def _status(entry: Dict[str, Any]) -> str:
    return str(entry.get("status", "")).strip().lower()


def _is_ready(entry: Dict[str, Any]) -> bool:
    return _status(entry) == "ready"


def _is_in_maintenance(entry: Dict[str, Any]) -> bool:
    return _status(entry) == "in maintenance"


# ---------------------------------------------------------------------------
# Per-model classification
# ---------------------------------------------------------------------------

def _classify(entry: Dict[str, Any]) -> str:
    """
    Classify a model for the health chart:

    - failing    : status is 'In Maintenance' (failed and flagged for fixing),
                   or status is 'Ready' with last_test_outcome fail/failed
    - not_tested : status is 'Ready' with no last_test_date
    - passing    : status is 'Ready' with last_test_outcome success
    """
    outcome = (entry.get("last_test_outcome") or "").strip().lower()
    if _is_in_maintenance(entry) and outcome in {"fail", "failed"}:
        return "failing"
    if _is_ready(entry):
        if not entry.get("last_test_date"):
            return "not_tested"
        if outcome == "success":
            return "passing"
    return "not_tested"


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def _compute_stats(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Compute aggregate statistics.

    Health breakdown covers Ready + In Maintenance models:
      - passing    : Ready + last_test_outcome success
      - not_tested : Ready + no last_test_date
      - failing    : In Maintenance, or Ready with a failing outcome
    Open-issue counts exclude Archived models.
    """
    total = len(data)
    archived_count = sum(1 for r in data if _status(r) == "archived")

    with_open_issues = 0
    for r in data:
        if _status(r) == "archived":
            continue
        try:
            if int(r.get("open_issues") or 0) > 0:
                with_open_issues += 1
        except (TypeError, ValueError):
            pass

    chartable = [r for r in data if _is_ready(r) or _is_in_maintenance(r)]
    ready_passing = ready_not_tested = ready_failing = 0
    for r in chartable:
        label = _classify(r)
        if label == "passing":
            ready_passing += 1
        elif label == "not_tested":
            ready_not_tested += 1
        else:
            ready_failing += 1

    return {
        "total_models": total,
        "archived": archived_count,
        "ready_total": sum(1 for r in data if _is_ready(r)),
        "ready_passing": ready_passing,
        "ready_not_tested": ready_not_tested,
        "ready_failing": ready_failing,
        "with_open_issues": with_open_issues,
    }


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------

def _get_current_month_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m")


def _get_previous_month_id() -> str:
    now = datetime.now(timezone.utc)
    last_day_prev = now.replace(day=1) - timedelta(days=1)
    return last_day_prev.strftime("%Y-%m")


def _get_all_repo_names(data: List[Dict[str, Any]]) -> Set[str]:
    return {str(r["repository_name"]) for r in data if r.get("repository_name")}


def _detect_added_models(
    data: List[Dict[str, Any]], month_id: str
) -> List[Dict[str, Any]]:
    added = []
    for r in data:
        lp = r.get("last_packaging_date")
        if not lp:
            continue
        try:
            dt = datetime.fromisoformat(str(lp))
        except ValueError:
            continue
        if dt.strftime("%Y-%m") == month_id:
            added.append({"repository_name": r.get("repository_name"), "slug": r.get("slug")})
    return added


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def _ax_style(ax) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#AAAAAA")
    ax.spines["bottom"].set_color("#AAAAAA")
    ax.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.4)
    ax.set_axisbelow(True)


def _build_trend_plots(history: List[Dict[str, Any]]) -> None:
    """
    Generate health_and_testing.png.

    One stacked bar chart showing, per month, the split of Ready models into:
        - Passing (tested + last outcome success)
        - Not tested (never tested by maintenance)
        - Failing (last outcome fail/failed)
    """
    if not history:
        return

    snapshots = sorted(history, key=lambda s: s.get("month", ""))
    months = [s["month"] for s in snapshots]
    totals_list = [s.get("totals", {}) for s in snapshots]

    passing    = [t.get("ready_passing",    t.get("healthy",  0)) for t in totals_list]
    not_tested = [t.get("ready_not_tested", t.get("outdated", 0)) for t in totals_list]
    failing    = [t.get("ready_failing",    t.get("failing",  0)) for t in totals_list]

    with_open_issues = [t.get("with_open_issues", 0) for t in totals_list]
    added_counts = [len(s.get("added_models", [])) for s in snapshots]

    x = list(range(len(months)))
    n = max(1, len(months))
    bar_width = 0.2 if n <= 2 else (0.35 if n <= 4 else 0.55)

    _ensure_reports_dir()

    # ── Figure 1: health breakdown ─────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(max(7, n * 1.4), 5))
    _ax_style(ax)

    bottom_not_tested = passing
    bottom_failing = [passing[i] + not_tested[i] for i in range(len(x))]

    ax.bar(x, passing,    width=bar_width, color=PALETTE[COL_PASSING],    label="Passing")
    ax.bar(x, not_tested, width=bar_width, bottom=bottom_not_tested,
           color=PALETTE[COL_NOT_TESTED], label="Not tested")
    ax.bar(x, failing,    width=bar_width, bottom=bottom_failing,
           color=PALETTE[COL_FAILING],    label="Failing")

    ax.set_title("Ready models: passing / not tested / failing", fontsize=13)
    ax.set_ylabel("Number of models")
    ax.set_xticks(x)
    ax.set_xticklabels(months, rotation=45, ha="right", fontsize=9)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3, frameon=False)

    fig.tight_layout()
    fig.savefig(HEALTH_TESTED_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)

    # ── Figure 2: open issues + packaged per month ────────────────────────
    fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 4), constrained_layout=True)
    for ax in (ax3, ax4):
        _ax_style(ax)

    ax3.plot(x, with_open_issues, marker="o", linewidth=2.0,
             color=PALETTE[3], label="Models with open issues")
    ax3.set_title("Models with open issues")
    ax3.set_ylabel("Number of models")
    ax3.set_xticks(x)
    ax3.set_xticklabels(months, rotation=45, ha="right")
    ax3.legend(frameon=False)

    ax4.bar(x, added_counts, color=PALETTE[6], label="New models")
    ax4.set_title("Packaged models per month")
    ax4.set_xticks(x)
    ax4.set_xticklabels(months, rotation=45, ha="right")

    fig.suptitle("Issues & growth", fontsize=13)
    fig.savefig(ISSUES_ADDED_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _build_distributions_figure(data: List[Dict[str, Any]]) -> None:
    """
    Two pie charts: source type and subtask distribution.
    Restricted to non-archived models with assigned values.
    """
    if not data:
        return

    def _counter(field: str) -> Counter:
        c: Counter = Counter()
        for r in data:
            if str(r.get("status", "")).strip().lower() == "archived":
                continue
            val = r.get(field)
            if val in (None, "", "null", "Unknown"):
                continue
            c[str(val)] += 1
        return c

    source_counter = _counter("source_type")
    task_counter = _counter("subtask")

    def _slice(counter: Counter, max_slices: int = 7):
        items = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)
        labels = [k for k, _ in items[:max_slices]]
        sizes  = [v for _, v in items[:max_slices]]
        if len(items) > max_slices:
            labels.append("Other")
            sizes.append(sum(v for _, v in items[max_slices:]))
        return labels or ["No data"], sizes or [1]

    s_labels, s_sizes = _slice(source_counter)
    t_labels, t_sizes = _slice(task_counter)

    def _truncate(label: str, n: int = 28) -> str:
        return label if len(label) <= n else label[:n - 1] + "…"

    s_labels_short = [_truncate(l) for l in s_labels]
    t_labels_short = [_truncate(l) for l in t_labels]

    colors = [PALETTE[i % len(PALETTE)] for i in range(max(len(s_labels), len(t_labels)))]

    _ensure_reports_dir()
    # Extra vertical room for the below-pie legends
    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(13, 8))
    fig.suptitle("Model distributions (active models)", fontsize=14, y=0.98)

    for ax, labels, sizes, title in (
        (ax_l, s_labels_short, s_sizes, "Source type"),
        (ax_r, t_labels_short, t_sizes, "Subtask"),
    ):
        wedges, _ = ax.pie(sizes, labels=None, colors=colors[:len(sizes)], startangle=90)
        ax.set_title(title, fontsize=12, pad=10)
        ax.axis("equal")
        # Legend below the pie, 2 columns, compact font
        ncol = min(2, len(labels))
        ax.legend(
            wedges, labels,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.04),
            ncol=ncol,
            fontsize=11,
            frameon=False,
        )

    fig.tight_layout(rect=[0.0, 0.0, 1.0, 0.95])
    fig.savefig(DISTRIBUTIONS_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def _build_monthly_markdown(
    month_id: str,
    snapshot: Dict[str, Any],
    history: List[Dict[str, Any]],
) -> str:
    t = snapshot["totals"]
    added = snapshot["added_models"]

    summary = "\n".join([
        f"- 📦 **Total models:** {t['total_models']}",
        f"  - 🗄️ **Archived:** {t.get('archived', '—')}",
        f"  - ✅ **Ready — passing:** {t['ready_passing']}",
        f"  - ⏳ **Ready — not yet tested:** {t['ready_not_tested']}",
        f"  - 🔴 **Ready — failing:** {t['ready_failing']}",
        f"- ❗ **Non-archived with open issues:** {t['with_open_issues']}",
    ])

    if added:
        header = "| 🧬 Repository | 🪪 Slug |\n|---------------|---------|\n"
        rows = "\n".join(f"| {m.get('repository_name','—')} | {m.get('slug','—')} |" for m in added)
        added_table = header + rows + "\n"
    else:
        added_table = "_No new models were packaged this month._\n"

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    return "\n".join([
        "# 📊 Monthly Health Report",
        "",
        f"**Month:** {month_id}  ",
        f"**Generated at:** {now_utc} (UTC)",
        "",
        "## 🔢 Snapshot",
        "",
        summary,
        "",
        "## 🆕 Models packaged this month",
        "",
        added_table,
        "## 📈 Trends over time",
        "",
        "### 🩺 Ready models: passing / not tested / failing",
        "",
        "![Health](./health_and_testing.png)",
        "",
        "### ❗ Issues & packaged models",
        "",
        "![Issues & added](./issues_and_added.png)",
        "",
        "### 🧩 Task & source type distributions",
        "",
        "![Distributions](./distributions_tasks_source.png)",
        "",
    ]) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    data = _load_repo_info()
    history = _load_history()

    month_id = _get_current_month_id()
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    totals = _compute_stats(data)
    all_repos = _get_all_repo_names(data)

    # Back-fill added_models for previous month if missing
    prev_month_id = _get_previous_month_id()
    prev_added = _detect_added_models(data, prev_month_id)
    for entry in history:
        if entry.get("month") == prev_month_id:
            entry["added_models"] = prev_added
            break

    added_models = _detect_added_models(data, month_id)

    snapshot = {
        "month": month_id,
        "generated_at": now_iso,
        "totals": totals,
        "added_models": added_models,
        "all_repositories": sorted(all_repos),
    }

    if history and history[-1].get("month") == month_id:
        history[-1] = snapshot
    else:
        history.append(snapshot)

    _save_history(history)
    _build_trend_plots(history)
    _build_distributions_figure(data)

    _ensure_reports_dir()
    MONTHLY_MD.write_text(_build_monthly_markdown(month_id, snapshot, history), encoding="utf-8")

    print(f"[ok] Monthly health report generated for {month_id}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
