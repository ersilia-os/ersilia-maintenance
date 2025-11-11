import os
import requests
from ersilia_maintenance.config import REPO_BASE_URL
from datetime import datetime, timezone
from typing import Optional, Tuple,Any


def _headers():
    tok = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')

    headers = {"Accept": "application/vnd.github.v3+json"}
    if tok:
        headers['Authorization'] =f'Bearer {tok}'
    return headers



