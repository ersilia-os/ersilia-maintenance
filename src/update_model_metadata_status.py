#!/usr/bin/env python3
"""
Update the Status field in a model's metadata file on GitHub via the Contents API.
Commits the change directly to the model repo (no local clone required).
"""
from __future__ import annotations

import sys
import json
import re
import base64
import argparse

from ersilia_maintenance.config import METADATA_FILENAMES, MODEL_OWNER
from ersilia_maintenance.github import _get_file_info, _put_file


def _set_status_in_json(content: str, status: str) -> str:
    data = json.loads(content)
    data["Status"] = status
    return json.dumps(data, indent=4) + "\n"


def _set_status_in_yaml(content: str, status: str) -> str:
    """Replace the Status line while preserving the rest of the file's formatting."""
    new_line = f"Status: {status}"
    updated = re.sub(r"^Status:[ \t]*.*$", new_line, content, flags=re.MULTILINE)
    if updated == content:
        # Field not present — append it
        updated = content.rstrip("\n") + f"\n{new_line}\n"
    return updated


def update_model_metadata(repo: str, status: str, token: str) -> bool:
    """
    Find the metadata file for *repo* and set its Status field to *status*.
    Returns True if the file was found and updated (or already had the right value).
    """
    for filename in METADATA_FILENAMES:
        info = _get_file_info(repo, filename, token)
        if info is None:
            continue

        sha = info["sha"]
        raw = base64.b64decode(info["content"]).decode("utf-8")

        if filename.endswith(".json"):
            updated = _set_status_in_json(raw, status)
        else:
            updated = _set_status_in_yaml(raw, status)

        if updated == raw:
            print(f"Status already '{status}' in {filename} for {repo}, no commit needed.")
            return True

        _put_file(
            repo,
            filename,
            updated,
            sha,
            f"Update Status to '{status}' [skip ci]",
            token,
        )
        print(f"Updated {filename} in {MODEL_OWNER}/{repo}: Status -> '{status}'")
        return True

    print(f"WARNING: No metadata file found in {MODEL_OWNER}/{repo}", file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Update the Status field in a model's metadata file on GitHub"
    )
    parser.add_argument("--model", required=True, help="Model identifier (e.g. eos1abc)")
    parser.add_argument("--status", required=True, help="New status value (e.g. 'In maintenance')")
    parser.add_argument(
        "--token",
        required=True,
        help="GitHub token with contents:write access to model repos",
    )
    args = parser.parse_args()

    ok = update_model_metadata(args.model, args.status, args.token)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
