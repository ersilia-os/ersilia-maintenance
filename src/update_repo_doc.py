# src/update_repo_doc.py
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

# File Paths
REPO_INFO = Path(__file__).parent.parent / "files" / "repo_info.json"
REPORT_MD = Path(__file__).parent.parent / "reports" / "model_report.md"

# Updated markers as requested
START_MARKER = "<------START TABLE"
END_MARKER = "<------END TABLE"


def _load_repo_info() -> List[Dict[str, Any]]:
    """Load metadata with error handling."""
    if not REPO_INFO.exists():
        return []
    try:
        return json.loads(REPO_INFO.read_text(encoding="utf-8"))
    except Exception:
        return []


def _format_field(value: Any, default: str = "—") -> str:
    """Format field or return dash."""
    if value in (None, "", "null"):
        return default
    return str(value)


def _format_open_issues(value: Any) -> str:
    """Format issues with colored icons."""
    try:
        n = int(value)
    except (TypeError, ValueError):
        return "❓"
    if n == 0: return f"🟢 {n}"
    if 1 <= n <= 4: return f"🟡 {n}"
    return f"🔴 {n}"


def _build_stats_summary(data: List[Dict[str, Any]]) -> str:
    """Build summary including In Progress and In Maintenance stats."""
    counts = {"archived": 0, "in progress": 0, "in maintenance": 0, "total": len(data)}
    issues_count = 0
    never_tested = 0

    for r in data:
        status = str(r.get("status", "")).strip().lower()
        
        if status in counts:
            counts[status] += 1
        
        # Logic: Track issues for everything EXCEPT 'archived' and 'in progress'
        if status not in ["archived", "in progress"]:
            try:
                if int(r.get("open_issues", 0)) > 0:
                    issues_count += 1
            except (TypeError, ValueError):
                pass

        if not r.get("last_test_date"):
            never_tested += 1

    # Healthy active models (Total non-archived/non-progress minus those with issues)
    active_health_total = counts["total"] - counts["archived"] - counts["in progress"]
    no_issues = active_health_total - issues_count

    return "\n".join([
        f"- 📦 **Total models:** {counts['total']}",
        f"  - 📂 **In progress:** {counts['in progress']}",
        f"  - 🛠️ **In maintenance:** {counts['in maintenance']}",
        f"  - 🗄️ **Archived:** {counts['archived']}",
        f"- ✅ **Active/Maintenance models with no issues:** {no_issues}",
        f"- ❗ **Active/Maintenance models with open issues:** {issues_count}",
        f"- 🧪 **Total models tested at least once:** {counts['total'] - never_tested}",
        f"- ⏳ **Total models never tested:** {never_tested}",
    ])


def _build_table_from_repo_info(data: List[Dict[str, Any]]) -> str:
    """Build the markdown table."""
    sorted_data = sorted(data, key=lambda r: str(r.get("repository_name", "")).lower())

    header = (
        "| 🧬 Repository | 🪪 Slug | 📍 Status | 📦 Last packaging | 🧪 Last test | 🔖 Release | ❗ Open issues |\n"
        "|---------------|---------|-----------|-------------------|--------------|------------|----------------|\n"
    )

    rows = []
    for r in sorted_data:
        status = _format_field(r.get("status"))
        # Only Archived gets a dash; Maintenance and Progress still show issue counts
        issue_col = "—" if status.lower() == "archived" else _format_open_issues(r.get("open_issues", 0))
        
        row = [
            _format_field(r.get("repository_name")),
            _format_field(r.get("slug")),
            status,
            _format_field(r.get("last_packaging_date")),
            _format_field(r.get("last_test_date")),
            _format_field(r.get("release")),
            issue_col
        ]
        rows.append(f"| {' | '.join(row)} |")

    return header + "\n".join(rows) + "\n"


def _build_block() -> str:
    """Build the full content block."""
    data = _load_repo_info()
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    
    return "\n".join([
        "## 📚 Model registry snapshot", "",
        f"_Last updated: **{now_utc}** (UTC)_", "",
        "### 🔢 Summary", "",
        _build_stats_summary(data), "",
        "The table below summarizes the current state of the models.", "",
        _build_table_from_repo_info(data)
    ])


def _inject_table(report_text: str, block_md: str) -> str:
    """
    Finds the first START and last END. 
    Replaces everything in between to clean up duplicate entries.
    """
    start_idx = report_text.find(START_MARKER)
    last_end_idx = report_text.rfind(END_MARKER) # Search from the end of the file backwards

    new_full_block = f"{START_MARKER}\n\n{block_md}\n\n{END_MARKER}"

    if start_idx != -1 and last_end_idx != -1 and last_end_idx > start_idx:
        # Replaces everything from the very first start to the very last end
        return (
            report_text[:start_idx] + 
            new_full_block + 
            report_text[last_end_idx + len(END_MARKER):]
        )
    
    # If markers are missing, append to end
    return report_text.strip() + f"\n\n{new_full_block}\n"


def main() -> int:
    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    
    if not REPORT_MD.exists():
        REPORT_MD.write_text("# 🛠️ Ersilia Maintenance Report\n", encoding="utf-8")

    new_block_content = _build_block()
    current_content = REPORT_MD.read_text(encoding="utf-8")
    
    updated_content = _inject_table(current_content, new_block_content)

    # Final write
    REPORT_MD.write_text(updated_content, encoding="utf-8")
    print(f"Update successful. Markers used: {START_MARKER} / {END_MARKER}")
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())