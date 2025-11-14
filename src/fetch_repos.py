# src/fetch_repos.py
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List
from ersilia_maintenance.github import _headers

import requests

# --- Config ---------------------------------------------------------------

API_URL = "https://api.github.com/orgs/ersilia-os/repos"
REPO_PATTERN = re.compile(r"^eos[a-zA-Z0-9]{4}$")
FILE_PATH = Path(__file__).parent.parent / "files" / "repo_info.json"
DEFAULT_RECENT_CHECK = "2000-01-01T00:00:00Z"

# --- IO helpers ------------------------------------------------------------

def _load_repo_info() -> List[Dict[str, Any]]:
    if FILE_PATH.exists():
        return json.loads(FILE_PATH.read_text(encoding="utf-8"))
    return []

def _save_repo_info(data: List[Dict[str, Any]]) -> None:
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    FILE_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# --- Fetch + merge ---------------------------------------------------------

def _fetch_all_repos() -> List[Dict[str, Any]]:
    """Fetch all repos from the org (paginated) and filter by pattern."""
    page = 1
    out: List[Dict[str, Any]] = []
    headers=_headers()

    while True:
        resp = requests.get(API_URL, headers=headers, params={"page": page})
        try:
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"[warn] Failed to fetch repositories (page {page}): {e}")
            break

        batch = resp.json()
        if not batch:
            break

        for repo in batch:
            name = repo["name"]
            if REPO_PATTERN.match(name):
                out.append(
                    {
                        "repository_name": repo["name"],
                        "last_updated": repo["updated_at"],
                        "most_recent_date_checked": DEFAULT_RECENT_CHECK,
                    }
                )
        page += 1

    print(f"[info] Fetched {len(out)} repositories matching pattern.")
    return out


def _ensure_fields(entry: Dict[str, Any]) -> Dict[str, Any]:
    """
    Make sure optional fields exist so later scripts don't crash.
    """
    # Core indexing fields
    entry.setdefault("repository_name", None)
    entry.setdefault("last_updated", None)
    entry.setdefault("most_recent_date_checked", DEFAULT_RECENT_CHECK)

    # Fields enriched by other steps/scripts
    entry.setdefault("slug", entry.get("slug"))  
    entry.setdefault("status", None)
    entry.setdefault("last_test_date", None)
    entry.setdefault("release", None)
    entry.setdefault("last_packaging_date", None)
    entry.setdefault("open_issues", None)
    entry.setdefault("issues_last_updated", None)
    return entry


def _merge(existing: List[Dict[str, Any]], fetched: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Merge fetched records into existing data while preserving any extra fields
    previously stored (release, last_packaging_date, open_issues, etc.).
    """
    by_name: Dict[str, Dict[str, Any]] = {e.get("repository_name"): _ensure_fields(dict(e)) for e in existing}

    for rec in fetched:
        name = rec["repository_name"]
        if name not in by_name:
            # New repository → seed with defaults + fetched core fields
            new_entry = _ensure_fields({})
            new_entry["repository_name"] = name
            new_entry["last_updated"] = rec.get("last_updated")
            new_entry["most_recent_date_checked"] = rec.get("most_recent_date_checked", DEFAULT_RECENT_CHECK)
            # Optional convenience: use name as slug by default
            by_name[name] = new_entry
        else:
            # Existing → update only what comes from GitHub index
            curr = by_name[name]
            # Update 'last_updated' if newer
            if rec.get("last_updated") and rec["last_updated"] != curr.get("last_updated"):
                curr["last_updated"] = rec["last_updated"]
            # Keep most_recent_date_checked unless you want to reset it here

    # Return sorted by repository_name for deterministic file diffs
    merged = list(by_name.values())
    merged.sort(key=lambda x: x.get("repository_name") or "")
    return merged

# --- Main -------------------------------------------------------------------

def main() -> int:
    existing = _load_repo_info()
    fetched = _fetch_all_repos()
    updated = _merge(existing, fetched)
    _save_repo_info(updated)
    print(f"[ok] Saved index to {FILE_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
