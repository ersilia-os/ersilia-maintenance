#!/usr/bin/env python3
"""Update the Status field of a model in Airtable."""
from __future__ import annotations

import sys
import argparse

AIRTABLE_MODEL_HUB_BASE_ID = "appR6ZwgLgG8RTdoU"
AIRTABLE_MODEL_HUB_TABLE_NAME = "Models"
AIRTABLE_PAGE_SIZE = 100
AIRTABLE_MAX_ROWS = 100000


def _find_record_id(table, model_id: str):
    for records in table.iterate(
        page_size=AIRTABLE_PAGE_SIZE, max_records=AIRTABLE_MAX_ROWS
    ):
        for record in records:
            try:
                if model_id == record["fields"].get("Identifier"):
                    return record["id"]
            except Exception:
                pass
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Update a model's Status field in Airtable"
    )
    parser.add_argument("--model", required=True, help="Model identifier (e.g. eos1abc)")
    parser.add_argument("--status", required=True, help="New status value")
    parser.add_argument("--api-key", required=True, help="Airtable API key (read-write)")
    args = parser.parse_args()

    try:
        from pyairtable import Api
    except ImportError:
        print(
            "ERROR: pyairtable is not installed. Run: pip install pyairtable",
            file=sys.stderr,
        )
        return 1

    api = Api(args.api_key)
    table = api.table(AIRTABLE_MODEL_HUB_BASE_ID, AIRTABLE_MODEL_HUB_TABLE_NAME)

    rec_id = _find_record_id(table, args.model)
    if rec_id is None:
        print(
            f"ERROR: Model '{args.model}' not found in Airtable", file=sys.stderr
        )
        return 1

    table.update(record_id=rec_id, fields={"Status": args.status})
    print(f"Updated '{args.model}' Status -> '{args.status}'")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
