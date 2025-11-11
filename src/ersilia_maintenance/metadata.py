from __future__ import annotations
import json
import os
import time
import yaml
import requests
import base64
from pathlib import Path
from typing import Any, Dict, Optional
from datetime import timezone, datetime
from ersilia_maintenance.github import _headers
from ersilia_maintenance.config import (
    REPO_BASE_URL,
    METADATA_FILENAMES,
    REQUEST_TIMEOUT,
    THROTTLE_DELAY,
    METADATA_TTL_SECONDS
)

SESSION = requests.Session()
SESSION.headers.update(_headers())

def should_refresh(field:str,entry: Dict[str, Any]) -> bool:
    if METADATA_TTL_SECONDS <= 0:
        return True
    ts = entry.get(field)
    if not ts:
        return True
    try:
        last = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except Exception:
        return True
    age = (datetime.now(timezone.utc) - last).total_seconds()
    return age >= METADATA_TTL_SECONDS


def load_metadata(repo:str)-> Optional[Dict[str,Any]]:
    """
    Looks for metadata.{yml|json} inside the model repo
    """

    for name in METADATA_FILENAMES:
        url = f"{REPO_BASE_URL}/{repo}/contents/{name}"
        r = SESSION.get(url,timeout=REQUEST_TIMEOUT)

        time.sleep(THROTTLE_DELAY)
        # Not found → try next candidate without raising
        if r.status_code == 404:
            continue

        # Other HTTP errors should surface
        r.raise_for_status()

        js = r.json()
        content_b64 = js.get("content")
        if not content_b64:
            continue  # no usable content, try next

        try:
            decoded = base64.b64decode(content_b64).decode("utf-8", "replace")
        except Exception:
            decoded = ""

        if not decoded:
            continue
        
        if name.endswith(".json"):
            print('metadata.json found')
            return json.loads(decoded)
        else:
            print('metadata.yml found')
            data = yaml.safe_load(decoded)
            return data or {}

    return None
    
def _extract_key(key:str,meta:Dict[str,Any])->str:
    if key in  meta:
        return str(meta[key])
    
    return None

def extract_release(meta: Dict[str,Any])-> Optional[str]:
    """Return Last Packaging Date from metadata if present."""
    return _extract_key('Release', meta)
    

def extract_last_packaging_date(meta: Dict[str,Any])-> Optional[str]:
    """Return Release from metadata if present."""
    return _extract_key('Last Packaging Date', meta)


def extract_slug(meta: Dict[str,Any])-> Optional[str]:
    """Return Slug from metadata if present."""
    return _extract_key('Slug', meta)

def extract_status(meta: Dict[str,Any])->Optional[str]:
    """Return Status from metadata if present."""
    return _extract_key('Status',meta)
