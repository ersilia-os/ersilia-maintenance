#!/usr/bin/env python3
"""Detect models whose upstream source code was updated after the model
was last packaged.

Source code URL handling:
  - any github.com/ersilia-os/* URL         → skip (maintained by us)
  - https://github.com/<owner>/<repo>       → walk commits since baseline;
                                              flag only if a non-.md file changed
  - https://pypi.org/project/<package>      → check latest release upload_time on PyPI
  - anything else                           → skip

No issues are opened by this script.
"""

from __future__ import annotations

import sys
import time
from datetime import datetime, timezone
from typing import Any
from urllib.parse import urlparse

import requests

from ersilia_maintenance.config import (
    DATE_FMT,
    GITHUB_API_BASE,
    REQUEST_TIMEOUT,
    ROOT_DIR,
    THROTTLE_DELAY,
)
from ersilia_maintenance.github import _headers
from ersilia_maintenance.io import load_repo_info

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

OUTPUT = ROOT_DIR / "reports" / "updated_models.md"
GITHUB_HOST = "github.com"
PYPI_HOST = "pypi.org"
SKIP_URL_SUBSTRINGS = {
    "rdkit",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _parse_github_repo(url: str) -> tuple[str, str] | None:
    """Extract (owner, repo) from a GitHub URL, or return None."""
    if not url:
        return None
    try:
        parsed = urlparse(url.strip().rstrip("/"))
    except Exception:
        return None
    if parsed.hostname != GITHUB_HOST:
        return None
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return None
    return parts[0], parts[1]


def _parse_pypi_package(url: str) -> str | None:
    """Extract package name from a PyPI URL, or return None.

    Handles https://pypi.org/project/<package> and
    https://pypi.org/project/<package>/<version>/.
    """
    try:
        parsed = urlparse(url.strip().rstrip("/"))
    except Exception:
        return None
    if parsed.hostname != PYPI_HOST:
        return None
    parts = [p for p in parsed.path.split("/") if p]
    # path is /project/<package> or /project/<package>/<version>
    if len(parts) >= 2 and parts[0] == "project":
        return parts[1]
    return None


MAX_COMMITS = 10  # max commits to inspect per repo


def _is_non_substantive(filename: str) -> bool:
    """Return True if a file should be ignored (docs or test files)."""
    lower = filename.lower()
    if lower.endswith(".md"):
        return True
    parts = lower.replace("\\", "/").split("/")
    # Skip files inside any test directory or whose name contains "test"
    return any("test" in part for part in parts)


def _has_code_changes(files: list[dict]) -> bool:
    """Return True if any changed file is a substantive (non-doc, non-test) file."""
    return any(not _is_non_substantive(f.get("filename", "")) for f in files)


def _fetch_github_last_code_commit(
    owner: str, repo: str, since: str, headers: dict
) -> str | None:
    """Return the date of the most recent non-.md commit after `since`, or None.

    Fetches up to MAX_COMMITS commits (newest-first) and checks each one's
    file list. Returns on the first commit that touches a non-.md file.
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits"
    try:
        resp = requests.get(
            url, headers=headers, timeout=REQUEST_TIMEOUT,
            params={"since": since, "per_page": MAX_COMMITS},
        )
        if resp.status_code == 404:
            print(f"[warn] GitHub repo not found: {owner}/{repo}", file=sys.stderr)
            return None
        resp.raise_for_status()
        commits = resp.json()
    except requests.RequestException as exc:
        print(f"[warn] Failed to list commits for {owner}/{repo}: {exc}", file=sys.stderr)
        return None

    for commit in commits:
        sha = commit.get("sha", "")
        commit_date = commit.get("commit", {}).get("committer", {}).get("date")
        time.sleep(THROTTLE_DELAY)
        try:
            detail = requests.get(
                f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits/{sha}",
                headers=headers, timeout=REQUEST_TIMEOUT,
            )
            detail.raise_for_status()
        except requests.RequestException:
            continue

        if _has_code_changes(detail.json().get("files", [])):
            return commit_date

    return None


def _fetch_pypi_latest_upload(package: str) -> str | None:
    """Return the upload_time of the latest release on PyPI, or None on error."""
    url = f"https://pypi.org/pypi/{package}/json"
    try:
        resp = requests.get(url, timeout=REQUEST_TIMEOUT)
        if resp.status_code == 404:
            print(f"[warn] PyPI package not found: {package}", file=sys.stderr)
            return None
        resp.raise_for_status()
        data = resp.json()
        latest_version = data.get("info", {}).get("version")
        releases = data.get("releases", {})
        files = releases.get(latest_version, [])
        if not files:
            return None
        # Take the earliest upload_time among the files of the latest release.
        times = [f["upload_time"] for f in files if f.get("upload_time")]
        return min(times) if times else None
    except requests.RequestException as exc:
        print(f"[warn] Failed to fetch PyPI {package}: {exc}", file=sys.stderr)
        return None


def _parse_dt(ts: str | None) -> datetime | None:
    """Parse ISO 8601 or YYYY-MM-DD string into an aware datetime."""
    if not ts:
        return None
    ts = ts.strip()
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except ValueError:
        pass
    # Date-only (YYYY-MM-DD) — treat as midnight UTC
    try:
        return datetime.strptime(ts, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    models: list[dict[str, Any]] = load_repo_info()
    gh_headers = _headers()
    flagged: list[dict[str, Any]] = []

    total = len(models)
    n_archived = n_no_url = n_skipped = n_no_baseline = n_unknown = 0
    checked = 0

    print(f"[info] Loaded {total} models from repo_info.json")

    for i, model in enumerate(models, 1):
        name = model.get("repository_name", "")
        status = model.get("status", "")
        source_url = (model.get("source_code_url") or "").strip().rstrip("/")

        if status == "Archived":
            n_archived += 1
            continue

        if not source_url:
            n_no_url += 1
            continue

        if any(s in source_url.lower() for s in SKIP_URL_SUBSTRINGS):
            n_skipped += 1
            continue

        # Skip any ersilia-os GitHub repo (they are maintained by us directly).
        gh = _parse_github_repo(source_url)
        if gh and gh[0].lower() == "ersilia-os":
            n_skipped += 1
            continue

        # Use last_packaging_date as the baseline; fall back to last_updated.
        baseline_raw = model.get("last_packaging_date") or model.get("last_updated")
        dt_baseline = _parse_dt(baseline_raw)
        if not dt_baseline:
            n_no_baseline += 1
            continue

        pypi_package = _parse_pypi_package(source_url)
        github_repo = _parse_github_repo(source_url)

        if pypi_package:
            source_type = "pypi"
        elif github_repo:
            source_type = "github"
        else:
            n_unknown += 1
            continue

        checked += 1
        print(f"  [{checked}] {name} ({source_type}) — {source_url}")

        upstream_ts: str | None = None
        if source_type == "pypi":
            time.sleep(THROTTLE_DELAY)
            upstream_ts = _fetch_pypi_latest_upload(pypi_package)
        else:
            owner, repo = github_repo
            since = dt_baseline.strftime(DATE_FMT)
            upstream_ts = _fetch_github_last_code_commit(owner, repo, since, gh_headers)

        dt_upstream = _parse_dt(upstream_ts)

        if dt_upstream and dt_upstream > dt_baseline:
            print(f"       → updated {upstream_ts} (packaged {baseline_raw}) ⚠")
            flagged.append(
                {
                    "repository_name": name,
                    "slug": model.get("slug", ""),
                    "status": status,
                    "source_code_url": source_url,
                    "source_type": source_type,
                    "last_packaging_date": model.get("last_packaging_date", ""),
                    "last_test_outcome": model.get("last_test_outcome", ""),
                    "upstream_updated_at": upstream_ts,
                }
            )
        else:
            print(f"       → up to date")

    print()
    print(f"[summary] {total} models total")
    print(f"          {n_archived} archived (skipped)")
    print(f"          {n_no_url} with no source code URL (skipped)")
    print(f"          {n_skipped} with an ersilia-os or known URL (skipped)")
    print(f"          {n_no_baseline} with no baseline date (skipped)")
    print(f"          {n_unknown} with an unrecognised URL type (skipped)")
    print(f"          {checked} checked → {len(flagged)} flagged as updated")

    flagged.sort(key=lambda m: m["upstream_updated_at"], reverse=True)

    # --- Write report -------------------------------------------------------
    now = datetime.now(timezone.utc).strftime(DATE_FMT)

    lines = [
        "# Updated Source Code Report",
        "",
        f"**Generated:** {now}",
        "",
        "Models whose upstream source code was updated **after** the model was last packaged.",
        f"Total: **{len(flagged)}**",
        "",
        "| Model | Slug | Status | Last Packaging Date | Last Test Outcome | Source | Source Updated At |",
        "|-------|------|--------|---------------------|-------------------|--------|-------------------|",
    ]

    for m in flagged:
        outcome = m["last_test_outcome"]
        icon = "✅" if outcome == "success" else ("🚨" if outcome in ("fail", "failed") else "❓")
        src = m["source_code_url"]
        src_label = f"[{m['source_type']}]({src})"
        lines.append(
            f"| {m['repository_name']} | {m['slug']} | {m['status']} "
            f"| {m['last_packaging_date']} | {icon} {outcome} "
            f"| {src_label} | {m['upstream_updated_at']} |"
        )

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[ok] Written {len(flagged)} model(s) to {OUTPUT}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
