# src/update_repo_doc.py
from __future__ import annotations
from pathlib import Path
import json
import re

REPO_INFO = Path("files/repo_info.json")
REPORT_MD = Path("reports/models_report.md")
README = Path("README.md")

START = "<!-- MODELS_TABLE_START -->"
END = "<!-- MODELS_TABLE_END -->"

def _load_table_from_report() -> str | None:
    if REPORT_MD.exists():
        return REPORT_MD.read_text(encoding="utf-8").strip()
    return None

def _build_table_from_repo_info() -> str:
    rows = []
    if REPO_INFO.exists():
        data = json.loads(REPO_INFO.read_text(encoding="utf-8"))
    else:
        data = []

    header = "| Repository Name | slug | Last packaging date | Last day tested | Release | Open issues |\n" \
             "|---|---|---|---|---|---|---|\n"
    for r in data:
        rows.append(
            f"| {r.get('repository_name','')} | {r.get('slug')} | "
            f" {r.get('last_packaging_date','')} | "
            f"{r.get('last_test_date','')} | {r.get('release','')} | {r.get('open_issues','')} |"
        )
    return header + "\n".join(rows) + ("\n" if rows else "")

def _inject_table(readme_text: str, table_md: str) -> str:
    pattern = re.compile(rf"({re.escape(START)})(.*?){re.escape(END)}", re.S)
    if pattern.search(readme_text):
        return pattern.sub(rf"\1\n{table_md}\n{END}", readme_text)
    # Si no hi ha marques, les afegim al final
    block = f"\n\n{START}\n{table_md}\n{END}\n"
    return readme_text + block

def main() -> int:
    table = _load_table_from_report()
    if not table:
        table = _build_table_from_repo_info()

    if not README.exists():
        README.write_text("# Ersilia Maintenance\n", encoding="utf-8")

    readme = README.read_text(encoding="utf-8")
    new_readme = _inject_table(readme, table)

    if new_readme != readme:
        README.write_text(new_readme, encoding="utf-8")
        print("README.md updated with models table.")
    else:
        print("README.md unchanged.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
