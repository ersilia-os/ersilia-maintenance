import yaml
import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from ersilia_maintenance.config import REPO_INFO_PATH

def read_yml(p:Path)->Dict[str,Any]:
    with p.open("r", encoding='utf-8') as f:
        return yaml.safe_load(f) or {}
    
def read_json(p:Path)->Dict[str,Any]:
    if not p.exists():
        return []
    with p.open("r", encoding='utf-8') as f:
        return json.load(f)

def save_json_file(file:Path, data:List[Dict[str, Any]]) ->None:
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def load_repo_info() -> List[Dict[str, Any]]:
    return json.loads(REPO_INFO_PATH.read_text(encoding="utf-8")) if REPO_INFO_PATH.exists() else []
