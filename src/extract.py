import json
import sys

BORDERS = ('┏', '┡', '├', '┝', '┯', '┠', '━', '┳', '┻', '─', '┼')
STATUS = ('✔ PASSED', '✘ FAILED')

def extract_summary(file_path):
    """
    Extracts a summary from a given result file.

    Parameters
    ----------
    file_path : str
        The path to the result file to be processed.

    Returns
    -------
    dict
        A dictionary containing the summary of checks with their status and details.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    Exception
        If there is an error during file processing.
    """
    summary, capturing, current_check = {}, False, None

    with open(file_path, 'r') as file:
        for line in file:
            if "Inspect Summary" in line:
                capturing = True
                continue

            if capturing:
                if line.startswith('└'):
                    break
                if line.strip().startswith(BORDERS):
                    continue

                if "│" in line:
                    parts = [part.strip() for part in line.strip().split("│")[1:-1]]
                    
                    if len(parts) == 2:
                        key, value = parts
                        if value in STATUS:
                            current_check = key
                            summary[current_check] = {"Status": value == STATUS[0], "Details": ""}
                        elif current_check:
                            summary[current_check]["Details"] += f" {key} {value}".strip()
                    elif len(parts) == 1 and current_check:
                        summary[current_check]["Details"] += f" {parts[0]}".strip()

    for check in summary:
        summary[check]["Details"] = summary[check]["Details"].strip()
    return summary

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract.py <path_to_result.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        summary = extract_summary(file_path)
        print(json.dumps(summary, indent=4))  
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)