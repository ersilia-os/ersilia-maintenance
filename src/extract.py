import json
import sys

def read_report(file) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract.py <path_to_result.json>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        report = read_report(file_path)
        print(json.dumps(report, indent=4))  
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
     