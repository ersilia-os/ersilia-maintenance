# src/pick_repo.py
from __future__ import annotations
import json
import random
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
from ersilia_maintenance.config import PICKED_FILE, COUNT, EXCLUDE_OPEN_ISSUES
from ersilia_maintenance.dates import parse_iso, days_since
from ersilia_maintenance.io import load_repo_info

# --- IO ---------------------------------------------------------------------

def _save_picked(rows: List[Dict[str, Any]]) -> None:
    PICKED_FILE.parent.mkdir(parents=True, exist_ok=True)
    PICKED_FILE.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# --- Elegibility-----------------------------------------------------------
def _eligible(entry: Dict[str, Any]) -> bool:

    oi = entry.get("open_issues")

    if EXCLUDE_OPEN_ISSUES and isinstance(oi, int) and oi > 0:
        return False
    
    status= entry.get('status')
    if status != 'Ready':
        return False
    
    return True

# --- Priority logic ---------------------------------------------------------

def _priority_key(entry: Dict[str, Any], now: datetime) -> tuple:
    """
    Sorting key:
    - First by whether it has ever been tested:
        * never tested (last_test_date is null) -> highest priority
    - Then by how long ago it was last tested:
        * older last_test_date -> higher priority

    Implemented as:
        (group, secondary)

    Where:
        group = 0 for never tested
                1 for tested with valid date
                2 for anything weird/unparseable (sent to the end)

        secondary:
            - for group 0: 0 (all never-tested together)
            - for group 1: -days_since (more days -> smaller -> comes first)
            - for group 2: 0
    """
    ts = entry.get("last_test_date")

    # Never tested
    if not ts:
        return (0, 0)

    ds = days_since(ts, now=now)

    # Valid date
    if ds is not None:
        # more days_since -> higher priority, so we use -ds for ascending sort
        return (1, -ds)
    
# --- Weakly pick ------------------------------------------------------

def pick_weekly(count: int = COUNT) -> List[Dict[str, Any]]:
    rows = load_repo_info()
    if not rows:
        _save_picked([])
        return []

    now = datetime.now(timezone.utc)

    candidates = [r for r in rows if _eligible(r)]

    if not candidates:
        _save_picked([])
        return []

    # Sort by priority: never tested first, then oldest last_test_date
    candidates.sort(key=lambda r: _priority_key(r, now=now))

    picked = candidates[:count]

    # Store a minimal, inspectable view (including a simple "priority_score")
    minimal: List[Dict[str, Any]] = []
    for r in picked:
        ts = r.get("last_test_date")
        ds = days_since(ts, now=now) if ts else None

        if ts is None:
            # Never tested: treat as max priority
            priority_score = 10**9
        elif ds is None:
            # Unparseable: neutral / low priority
            priority_score = 0
        else:
            # Larger "days since last test" = higher priority
            priority_score = ds

        minimal.append(
            {
                "repository_name": r["repository_name"],
                "slug": r.get("slug"),
                "priority_score": priority_score,
                "last_test_date": ts,
                "last_packaging_date": r.get("last_packaging_date"),
                "open_issues": r.get("open_issues"),
            }
        )

    _save_picked(minimal)
    return minimal


def main() -> int:
    picked = pick_weekly()

    if picked:
        for r in picked:
            print(r["repository_name"])
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
