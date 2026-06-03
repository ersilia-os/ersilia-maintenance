#!/usr/bin/env python3
"""
Update the Publication field in a model's metadata file on GitHub via the Contents API.
Commits the change directly to the model repo (no local clone required).
"""
from __future__ import annotations

import re
import sys
import json
import base64
import argparse

from ersilia_maintenance.config import METADATA_FILENAMES, MODEL_OWNER
from ersilia_maintenance.github import _get_file_info, _put_file

_PROXY_RE = re.compile(r"https?://doi-org\.[^/]+/")


def normalize_doi(url: str) -> str:
    """Canonicalize DOI URLs: fix institutional proxies and strip trailing punctuation."""
    url = url.strip()
    url = _PROXY_RE.sub("https://doi.org/", url)
    url = url.rstrip(".,;")
    return url


def _set_publication_in_json(content: str, url: str) -> str:
    data = json.loads(content)
    data["Publication"] = url
    return json.dumps(data, indent=4) + "\n"


def _set_publication_in_yaml(content: str, url: str) -> str:
    new_line = f"Publication: {url}"
    updated = re.sub(r"^Publication:[ \t]*.*$", new_line, content, flags=re.MULTILINE)
    if updated == content:
        updated = content.rstrip("\n") + f"\n{new_line}\n"
    return updated


def get_current_publication(repo: str, token: str) -> str | None:
    """Return the current Publication value from the model's metadata, or None if not found."""
    for filename in METADATA_FILENAMES:
        info = _get_file_info(repo, filename, token)
        if info is None:
            continue
        raw = base64.b64decode(info["content"]).decode("utf-8")
        if filename.endswith(".json"):
            data = json.loads(raw)
            return data.get("Publication")
        else:
            m = re.search(r"^Publication:[ \t]*(.*)$", raw, flags=re.MULTILINE)
            return m.group(1).strip() if m else None
    return None


def update_model_publication(repo: str, url: str, token: str, dry_run: bool = False) -> str:
    """
    Find the metadata file for *repo* and set its Publication field to *url*.

    Returns one of: "updated", "already_correct", "not_found", "dry_run".
    """
    url = normalize_doi(url)

    for filename in METADATA_FILENAMES:
        info = _get_file_info(repo, filename, token)
        if info is None:
            continue

        sha = info["sha"]
        raw = base64.b64decode(info["content"]).decode("utf-8")

        if filename.endswith(".json"):
            updated = _set_publication_in_json(raw, url)
        else:
            updated = _set_publication_in_yaml(raw, url)

        if updated == raw:
            print(f"Publication already '{url}' in {filename} for {repo}, no commit needed.")
            return "already_correct"

        if dry_run:
            return "dry_run"

        _put_file(
            repo,
            filename,
            updated,
            sha,
            f"Update Publication to DOI link [skip ci]",
            token,
        )
        print(f"Updated {filename} in {MODEL_OWNER}/{repo}: Publication -> '{url}'")
        return "updated"

    print(f"WARNING: No metadata file found in {MODEL_OWNER}/{repo}", file=sys.stderr)
    return "not_found"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Update the Publication field in a model's metadata file on GitHub"
    )
    parser.add_argument("--model", required=True, help="Model identifier (e.g. eos1abc)")
    parser.add_argument("--publication", required=True, help="New publication DOI URL")
    parser.add_argument(
        "--token",
        required=True,
        help="GitHub token with contents:write access to model repos",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without committing")
    args = parser.parse_args()

    result = update_model_publication(args.model, args.publication, args.token, dry_run=args.dry_run)
    return 0 if result in ("updated", "already_correct", "dry_run") else 1


if __name__ == "__main__":
    raise SystemExit(main())
