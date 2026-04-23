from __future__ import annotations
from typing import List, Tuple
from ersilia_maintenance.io import load_repo_info
from ersilia_maintenance.metadata import load_metadata, extract_contributor


def main() -> int:
    data = load_repo_info()
    if not data:
        print("[warn] files/repo_info.json not found or empty")
        return 0

    no_metadata: List[Tuple[str, str]] = []
    missing_contributor: List[Tuple[str, str]] = []

    for e in data:
        repo = e.get("repository_name")
        if not repo:
            continue
        status = e.get("status") or "Unknown"
        print(f"[LOG] checking contributor for {repo}")
        meta = load_metadata(repo=repo)
        if meta is None:
            no_metadata.append((repo, status))
            continue
        contributor = extract_contributor(meta)
        if not contributor:
            missing_contributor.append((repo, status))

    all_missing = no_metadata + missing_contributor
    archived_count = sum(1 for _, s in all_missing if s == "Archived")

    if no_metadata:
        print(f"\n--- No metadata file found ({len(no_metadata)}) ---")
        for repo, status in no_metadata:
            print(f"  {repo}  [status: {status}]")

    if missing_contributor:
        print(f"\n--- Missing Contributor field ({len(missing_contributor)}) ---")
        for repo, status in missing_contributor:
            print(f"  {repo}  [status: {status}]")

    print(f"\n--- Summary ---")
    print(f"Total models checked : {len(data)}")
    print(f"Missing contributor  : {len(all_missing)}")
    print(f"  of which Archived  : {archived_count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
