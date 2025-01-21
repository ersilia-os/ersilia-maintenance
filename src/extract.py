import json
import sys
from pathlib import Path

file_path = Path.cwd() / "eos4e40-test.json"

def read_report(file) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
try:
    report = read_report(file_path)
    print(json.dumps(report, indent=4))  
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)