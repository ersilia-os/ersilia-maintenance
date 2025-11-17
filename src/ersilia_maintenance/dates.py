from datetime import datetime, timezone
from ersilia_maintenance.config import DATE_FMT
from typing import Optional

def now_iso() -> str:
    return datetime.now(timezone.utc).strftime(DATE_FMT)

# --- Helpers de temps -------------------------------------------------------
def parse_iso(ts: Optional[str]) -> Optional[datetime]:
    if not ts:
        return None
    try:
        if ts.endswith("Z"):
            ts = ts[:-1]
            dt = datetime.fromisoformat(ts)
            return dt.replace(tzinfo=timezone.utc)
        return datetime.fromisoformat(ts).replace(tzinfo=timezone.utc)
    except Exception:
        # fallback a format clàssic 
        try:
            return datetime.strptime(ts, DATE_FMT).replace(tzinfo=timezone.utc)
        except Exception:
            return None


def days_since(ts: Optional[str], now: Optional[datetime] = None) -> Optional[int]:
    dt = parse_iso(ts)
    if not dt:
        return None
    if not now:
        now = datetime.now(timezone.utc)
    return max(0, int((now - dt).total_seconds() // 86400))
