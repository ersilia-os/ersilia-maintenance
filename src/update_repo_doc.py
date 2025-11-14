# src/update_repo_doc.py
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

REPO_INFO = Path(__file__).parent.parent / "files" / "repo_info.json"
REPORT_MD = Path(__file__).parent.parent / "reports" / "model_report.md"

START = "<!-- MODELS_TABLE_START -->"
END = "<!-- MODELS_TABLE_END -->"


def _load_repo_info() -> List[Dict[str, Any]]:
    """
    Load repository metadata from the repo_info.json file.

    Returns:
        List[Dict[str, Any]]: A list of repository metadata dictionaries.
    """
    if not REPO_INFO.exists():
        return []
    return json.loads(REPO_INFO.read_text(encoding="utf-8"))


def _format_field(value: Any, default: str = "—") -> str:
    """
    Format a generic field for Markdown output.

    Args:
        value (Any): The value to format.
        default (str, optional): Default text when value is missing or empty.

    Returns:
        str: A user-friendly string representation.
    """
    if value in (None, "", "null"):
        return default
    return str(value)


def _format_open_issues(value: Any) -> str:
    """
    Format the open issues count with a colored icon.

    Rules:
        - 0   -> 🟢 0
        - 1-4 -> 🟡 n
        - 5+  -> 🔴 n

    Args:
        value (Any): The open issues value.

    Returns:
        str: A formatted string with an emoji and the count.
    """
    try:
        n = int(value)
    except (TypeError, ValueError):
        return "❓"

    if n == 0:
        return f"🟢 {n}"
    if 1 <= n <= 4:
        return f"🟡 {n}"
    return f"🔴 {n}"


def _build_stats_summary(data: List[Dict[str, Any]]) -> str:
    """
    Build a small stats summary block for the model registry.

    Stats included:
        - Total models
        - Models with no open issues
        - Models with open issues
        - Models never tested

    Args:
        data (List[Dict[str, Any]]): Repository metadata entries.

    Returns:
        str: A Markdown-formatted bullet list.
    """
    total = len(data)

    with_open_issues = 0
    never_tested = 0

    for r in data:
        oi = r.get("open_issues")
        try:
            oi_int = int(oi) if oi is not None else 0
        except (TypeError, ValueError):
            oi_int = 0

        if oi_int > 0:
            with_open_issues += 1

        last_test = r.get("last_test_date")
        if not last_test:
            never_tested += 1

    no_open_issues = total - with_open_issues
    tested_at_least_once = total - never_tested

    lines = [
        f"- 📦 **Total models:** {total}",
        f"- ✅ **Models with no open issues:** {no_open_issues}",
        f"- ❗ **Models with open issues:** {with_open_issues}",
        f"- 🧪 **Models tested at least once:** {tested_at_least_once}",
        f"- ⏳ **Models never tested:** {never_tested}",
    ]
    return "\n".join(lines)


def _build_table_from_repo_info(data: List[Dict[str, Any]]) -> str:
    """
    Build a Markdown table summarizing repository information.

    The table includes:
        - repository_name
        - slug
        - last_packaging_date
        - last_test_date
        - release
        - open_issues (with colored icons)

    Args:
        data (List[Dict[str, Any]]): Repository metadata entries.

    Returns:
        str: A Markdown-formatted table.
    """
    # Sort repositories alphabetically by name for a stable view
    data = sorted(
        data,
        key=lambda r: _format_field(r.get("repository_name", "")).lower()
    )

    header = (
        "| 🧬 Repository | 🪪 Slug | 📦 Last packaging | 🧪 Last test | 🔖 Release | ❗ Open issues |\n"
        "|---------------|---------|-------------------|--------------|------------|----------------|\n"
    )

    rows: List[str] = []
    for r in data:
        rows.append(
            "| "
            + " | ".join(
                [
                    _format_field(r.get("repository_name")),
                    _format_field(r.get("slug")),
                    _format_field(r.get("last_packaging_date")),
                    _format_field(r.get("last_test_date")),
                    _format_field(r.get("release")),
                    _format_open_issues(r.get("open_issues", 0)),
                ]
            )
            + " |"
        )

    return header + ("\n".join(rows) + "\n" if rows else "")


def _build_block() -> str:
    """
    Build the full Markdown block to inject between markers.

    The block includes:
        - A heading
        - A "Last updated" timestamp in UTC
        - A small stats summary
        - The models table
    """
    data = _load_repo_info()
    table_md = _build_table_from_repo_info(data)
    stats_md = _build_stats_summary(data)

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    block = (
        "## 📚 Model registry snapshot\n\n"
        f"_Last updated: **{now_utc}** (UTC)_\n\n"
        "### 🔢 Summary\n\n"
        f"{stats_md}\n\n"
        "The table below summarizes the current state of the models tracked in "
        "`repo_info.json`.\n\n"
        + table_md
    )
    return block


def _inject_table(report_text: str, block_md: str) -> str:
    """
    Inject the generated block into the report between START and END markers.

    If the markers do not exist, they are appended at the end of the document.

    Args:
        report_text (str): Existing report markdown text.
        block_md (str): Markdown block to inject.

    Returns:
        str: Updated report markdown text.
    """
    pattern = re.compile(rf"({re.escape(START)})(.*?){re.escape(END)}", re.S)

    if pattern.search(report_text):
        # Replace existing block (anything between START and END) with the new block
        return pattern.sub(rf"\1\n{block_md}\n{END}", report_text)

    # If markers are not present, append the block at the end
    block = f"\n\n{START}\n{block_md}\n{END}\n"
    return report_text + block


def main() -> int:
    """
    Entry point to update the model report markdown file.

    The function:
        - Builds a Markdown block from repo_info.json.
        - Ensures the report file exists.
        - Injects or updates the block between the START/END markers.
    """
    block = _build_block()

    if not REPORT_MD.exists():
        REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
        REPORT_MD.write_text("# 🛠️ Ersilia Maintenance Report\n", encoding="utf-8")

    report = REPORT_MD.read_text(encoding="utf-8")
    new_report = _inject_table(report, block)

    if new_report != report:
        REPORT_MD.write_text(new_report, encoding="utf-8")
        print("model_report.md updated with models table.")
    else:
        print("model_report.md unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
