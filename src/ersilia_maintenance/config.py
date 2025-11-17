from __future__ import annotations
import os
from pathlib import Path

# --- GitHub / API ----------------------------------------------------------
# Model Owner
MODEL_OWNER: str = os.getenv("MODEL_OWNER", "ersilia-os")

# Base API URLs
GITHUB_API_BASE = "https://api.github.com"
ORG_REPOS_URL = f"{GITHUB_API_BASE}/orgs/{MODEL_OWNER}/repos"
REPO_BASE_URL = f"{GITHUB_API_BASE}/repos/{MODEL_OWNER}"

# --- Paths ----------------------------------------------------------------

ROOT_DIR = Path(__file__).parent.parent.parent
FILES_DIR = ROOT_DIR / "files"
REPO_INFO_PATH = FILES_DIR / "repo_info.json"
PICKED_FILE = FILES_DIR / "picked_weekly.json"
COMMON_MODELS_FILE = FILES_DIR / "common_models.json"

# --- Metadata --------------------------------------------------------------

# TTL for metadata refresh (seconds). Default 0 = always refresh
METADATA_TTL_SECONDS: int = int(os.getenv("METADATA_TTL_SECONDS", "0"))
METADATA_FILENAMES = ["metadata.yml", "metadata.json"]
# --- Patterns --------------------------------------------------------------

# Regex for repository naming (e.g. eosxxxx)
REPO_PATTERN = r"^eos[a-zA-Z0-9]{4}$"
DATE_FMT = "%Y-%m-%dT%H:%M:%SZ"
# --- Misc -----------------------------------------------------------------

DEFAULT_RECENT_CHECK = "2000-01-01T00:00:00Z"
REQUEST_TIMEOUT = 30   # seconds
THROTTLE_DELAY = 0.15  # seconds between GitHub requests
PER_PAGE = 100         # pagination size

#----Model Picking-----------------------------------------------------------
COUNT = int(os.getenv("WEEKLY_SHALLOW_COUNT", "10"))
EXCLUDE_OPEN_ISSUES = os.getenv("EXCLUDE_OPEN_ISSUES", "true").lower() in {"1", "true", "yes"}
                        # per random estable (opcional)

#-----Health report

# Health classification thresholds (can be tuned later)
HEALTH_RECENT_DAYS = 90   # days since last test to be considered "recent"
OUTDATED_DAYS = 200       # days since last test to be considered "outdated"

# Corporate color palette
PALETTE = [
    "#50285A",  
    "#FAD782",  
    "#FAA08B",  
    "#DC9FDC",
    "#AA96FA",
    "#8DC7FA",
    "#BEE6B4",
    "#D2D2D2",
]
