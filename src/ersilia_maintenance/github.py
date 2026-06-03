import base64
import os
import requests
from ersilia_maintenance.config import GITHUB_API_BASE, MODEL_OWNER, REQUEST_TIMEOUT
from datetime import datetime, timezone
from typing import Any

BOT_NAME = "ersilia-bot"
BOT_EMAIL = "ersilia-bot@users.noreply.github.com"


def _headers(token: str | None = None) -> dict:
    tok = token or os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github.v3+json"}
    if tok:
        headers["Authorization"] = f"Bearer {tok}"
    return headers


def _get_file_info(repo: str, path: str, token: str) -> dict | None:
    """Return the file info dict from the GitHub Contents API, or None if not found."""
    url = f"{GITHUB_API_BASE}/repos/{MODEL_OWNER}/{repo}/contents/{path}"
    r = requests.get(url, headers=_headers(token), timeout=REQUEST_TIMEOUT)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return r.json()


def _put_file(
    repo: str, path: str, new_content: str, sha: str, message: str, token: str
) -> Any:
    """Commit an updated file via the GitHub Contents API."""
    url = f"{GITHUB_API_BASE}/repos/{MODEL_OWNER}/{repo}/contents/{path}"
    payload = {
        "message": message,
        "content": base64.b64encode(new_content.encode("utf-8")).decode("ascii"),
        "sha": sha,
        "author": {"name": BOT_NAME, "email": BOT_EMAIL},
        "committer": {"name": BOT_NAME, "email": BOT_EMAIL},
    }
    r = requests.put(url, json=payload, headers=_headers(token), timeout=REQUEST_TIMEOUT)
    r.raise_for_status()
    return r.json()
