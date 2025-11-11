# src/refresh_open_issues.py
from __future__ import annotations
import sys
import requests
from typing import Any, Dict
import time
from ersilia_maintenance.config import REPO_BASE_URL, THROTTLE_DELAY, REPO_INFO_PATH
from ersilia_maintenance.github import _headers
from ersilia_maintenance.io import load_repo_info, save_json_file
from ersilia_maintenance.dates import now_iso
from ersilia_maintenance.metadata import should_refresh


def count_open_issues(repo:str)->int:
    """
    Counts the number of open issues
    """
    r= requests.get(f'{REPO_BASE_URL}/{repo}', headers=_headers())
    return r.json()['open_issues_count']


def main() -> int:
    data = load_repo_info()
    if not data:
        print("[warn] files/repo_info.json not found or empty", file=sys.stderr)
        return 0

    changed = False
    for e in data:
        repo = e.get("repository_name")
        if not repo:
            continue
        if not should_refresh("issues_last_updated",e):
            continue
        try:
            total = count_open_issues(repo)
            e["open_issues"] = total
            e["issues_last_updated"] = now_iso()
            changed = True
        except requests.HTTPError as err:
            print(f"[warn] HTTP error for {repo}: {err}", file=sys.stderr)
            e["open_issues"] = -1
            e["issues_last_updated"] = now_iso()
            changed = True
        except Exception as err:
            print(f"[warn] error for {repo}: {err}", file=sys.stderr)
            e["open_issues"] = -1
            e["issues_last_updated"] = now_iso()
            changed = True

        time.sleep(THROTTLE_DELAY)

    if changed:
        save_json_file(REPO_INFO_PATH, data)
        print("files/repo_info.json updated")
    else:
        print("no changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
