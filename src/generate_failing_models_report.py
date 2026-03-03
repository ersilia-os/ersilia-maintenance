#!/usr/bin/env python3
"""Generate reports/failing_models.md from files/repo_info.json.

Includes all non-Archived models whose last_test_outcome is a failure
("fail" or "failed"), sorted by most-recent test date first.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

REPO_INFO = Path("files/repo_info.json")
OUTPUT = Path("reports/failing_models.md")

FAIL_VALUES = {"fail", "failed"}


def main():
    with open(REPO_INFO) as f:
        models = json.load(f)

    failing = [
        m for m in models
        if m.get("last_test_outcome") in FAIL_VALUES
        and m.get("status") != "Archived"
    ]

    failing.sort(key=lambda m: m.get("last_test_date") or "", reverse=True)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "# Failing Models Report",
        "",
        f"**Generated:** {now}",
        "",
        f"Models with a failing last test outcome (Archived models excluded). "
        f"Total: **{len(failing)}**",
        "",
        "| Model | Slug | Status | Last Test Date | Outcome |",
        "|-------|------|--------|----------------|---------|",
    ]

    for m in failing:
        name = m.get("repository_name", "")
        slug = m.get("slug", "")
        status = m.get("status", "")
        test_date = m.get("last_test_date", "")
        outcome = m.get("last_test_outcome", "")
        lines.append(f"| {name} | {slug} | {status} | {test_date} | 🚨 {outcome} |")

    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"Written {len(failing)} failing model(s) to {OUTPUT}")


if __name__ == "__main__":
    main()
