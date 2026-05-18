#!/usr/bin/env python3
"""
Push a locally-generated README.md to a model repo via the GitHub Contents API.
Intended to be called after `airtableops.py readme-update` has written the file locally.
"""
from __future__ import annotations

import sys
import argparse
from pathlib import Path

from update_model_publication import _get_file_info, _put_file


def update_model_readme(repo: str, readme_path: Path, token: str) -> bool:
    new_content = readme_path.read_text(encoding="utf-8")

    info = _get_file_info(repo, "README.md", token)
    if info is None:
        print(f"WARNING: README.md not found in ersilia-os/{repo}", file=sys.stderr)
        return False

    sha = info["sha"]

    import base64
    current = base64.b64decode(info["content"]).decode("utf-8")
    if current == new_content:
        print(f"README.md already up to date for {repo}, no commit needed.")
        return True

    _put_file(
        repo,
        "README.md",
        new_content,
        sha,
        "Update README with new publication DOI link [skip ci]",
        token,
    )
    print(f"Updated README.md in ersilia-os/{repo}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Push a locally-generated README.md to a model repo"
    )
    parser.add_argument("--model", required=True, help="Model identifier (e.g. eos1abc)")
    parser.add_argument("--file", required=True, type=Path, help="Path to the local README.md")
    parser.add_argument("--token", required=True, help="GitHub token with contents:write access")
    args = parser.parse_args()

    ok = update_model_readme(args.model, args.file, args.token)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
