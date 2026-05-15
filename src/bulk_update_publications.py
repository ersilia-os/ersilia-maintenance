#!/usr/bin/env python3
"""
Bulk-update the Publication field in all model repos listed in the DOI CSV.

Skips rows where:
  - doi is "-" or empty
  - publication_type is "Other" or empty

Dry-run mode fetches the current Publication value from each model repo and
prints a table: model_id | current_publication | new_doi_url
"""
from __future__ import annotations

import csv
import sys
import argparse
from pathlib import Path

from update_model_publication import (
    get_current_publication,
    normalize_doi,
    update_model_publication,
)

DEFAULT_CSV = Path(__file__).parent.parent / "files" / "ErsiliaModelsDOI.csv"


def _should_skip(row: dict) -> str | None:
    """Return a skip reason string, or None if the row should be processed."""
    doi = row.get("doi", "").strip()
    pub_type = row.get("publication_type", "").strip()

    if not doi or doi == "-":
        return "no DOI"
    if not pub_type or pub_type.lower() == "other":
        return "publication type is Other/empty"
    return None


def run(
    csv_path: Path,
    token: str,
    dry_run: bool,
    model_filter: str | None,
    output_updated: Path | None = None,
) -> int:
    counts = {"updated": 0, "already_correct": 0, "skipped": 0, "failed": 0, "dry_run": 0}
    dry_run_rows: list[tuple[str, str, str]] = []
    updated_models: list[str] = []

    with open(csv_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)

    if model_filter:
        rows = [r for r in rows if r.get("model_id", "").strip() == model_filter]
        if not rows:
            print(f"No row found for model_id '{model_filter}'", file=sys.stderr)
            return 1

    for row in rows:
        model_id = row.get("model_id", "").strip()
        if not model_id:
            continue

        skip_reason = _should_skip(row)
        if skip_reason:
            print(f"SKIP  {model_id}: {skip_reason}")
            counts["skipped"] += 1
            continue

        doi = normalize_doi(row["doi"].strip())

        if dry_run:
            try:
                current = get_current_publication(model_id, token) or "(not set)"
            except Exception as exc:
                current = f"(fetch error: {exc})"
                counts["failed"] += 1
            dry_run_rows.append((model_id, current, doi))
            counts["dry_run"] += 1
        else:
            try:
                result = update_model_publication(model_id, doi, token, dry_run=False)
                counts[result] = counts.get(result, 0) + 1
                if result == "updated":
                    updated_models.append(model_id)
            except Exception as exc:
                print(f"ERROR {model_id}: {exc}", file=sys.stderr)
                counts["failed"] += 1

    if output_updated is not None and not dry_run:
        output_updated.write_text("\n".join(updated_models) + ("\n" if updated_models else ""))
        print(f"Written {len(updated_models)} updated model IDs to {output_updated}")

    if dry_run and dry_run_rows:
        col_w = [
            max(len("model_id"), max(len(r[0]) for r in dry_run_rows)),
            max(len("current_publication"), max(len(r[1]) for r in dry_run_rows)),
            max(len("new_doi_url"), max(len(r[2]) for r in dry_run_rows)),
        ]
        header = f"{'model_id':<{col_w[0]}}  {'current_publication':<{col_w[1]}}  {'new_doi_url':<{col_w[2]}}"
        sep = "  ".join("-" * w for w in col_w)
        print("\n" + header)
        print(sep)
        for model_id, current, doi in dry_run_rows:
            marker = "  (same)" if current == doi else ""
            print(f"{model_id:<{col_w[0]}}  {current:<{col_w[1]}}  {doi:<{col_w[2]}}{marker}")

    print(
        f"\nSummary: {counts['updated']} updated, "
        f"{counts['already_correct']} already correct, "
        f"{counts['skipped']} skipped (no DOI / Other), "
        f"{counts['failed']} failed"
        + (f", {counts['dry_run']} dry-run rows" if dry_run else "")
    )

    return 1 if counts["failed"] > 0 else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bulk-update Publication field to DOI URLs in all Ersilia model repos"
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help="Path to the DOI CSV file (default: files/ErsiliaModelsDOI - Sheet1.csv)",
    )
    parser.add_argument(
        "--token",
        required=True,
        help="GitHub token with contents:write access to model repos",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch current values and print a diff table without committing",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Limit to a single model ID (for testing)",
    )
    parser.add_argument(
        "--output-updated",
        type=Path,
        default=None,
        help="Write successfully-updated model IDs (one per line) to this file",
    )
    args = parser.parse_args()

    return run(args.csv, args.token, args.dry_run, args.model, args.output_updated)


if __name__ == "__main__":
    raise SystemExit(main())
