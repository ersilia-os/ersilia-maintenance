# src/update_from_metadata.py
from __future__ import annotations
from typing import Any, Dict
from ersilia_maintenance.config import REPO_INFO_PATH
from ersilia_maintenance.dates import now_iso
from ersilia_maintenance.io import save_json_file, load_repo_info
from ersilia_maintenance.metadata import (
    load_metadata,
    extract_release,
    extract_last_packaging_date,
    extract_slug,
    extract_status,
    extract_subtask,
    extract_source_type,
    should_refresh
)

def _ensure_defaults(e: Dict[str, Any]) -> None:
    # camps que altres scripts poden necessitar
    e.setdefault("repository_name", None)
    e.setdefault("slug", e.get("repository_name"))
    e.setdefault("release", None)
    e.setdefault("last_packaging_date", None)
    e.setdefault("status", None)
    e.setdefault("metadata_last_updated", None)
    e.setdefault("subtask",None)
    e.setdefault("source_type", None)

def main() -> int:
    data = load_repo_info()
    if not data:
        print("[warn] files/repo_info.json not found or empty")
        return 0

    changed = False
    for e in data:
        _ensure_defaults(e)
        repo = e.get("repository_name")
        if not repo:
            continue
        if not should_refresh("metadata_last_updated",e):
            continue

        # Load metadata
        print(f'[LOG] extracting metadata {repo}')
        meta = load_metadata(repo=repo)

        if not meta:
            e["metadata_last_updated"] = now_iso()
            changed = True
            continue

        # Extreure camps des de la metadata
        rel  = extract_release(meta)
        pack = extract_last_packaging_date(meta)
        slug = extract_slug(meta)
        stat = extract_status(meta)
        task = extract_subtask(meta)
        source = extract_source_type(meta)

        if rel is not None:   e["release"] = rel
        if pack is not None:  e["last_packaging_date"] = pack
        if slug is not None:  e["slug"] = slug
        if e["status"] != "Archived":
            if stat is not None:  e["status"] = stat
        if task is not None: e['subtask'] = task
        if source is not None: e["source_type"] = source

        e["metadata_last_updated"] = now_iso()
        changed = True

    if changed:
        save_json_file(REPO_INFO_PATH,data)
        print("files/repo_info.json updated from metadata")
    else:
        print("no changes from metadata")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
