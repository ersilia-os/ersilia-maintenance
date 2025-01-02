import json
import sys

BORDERS = ("┏", "┡", "├", "┝", "┯", "┠", "━", "┳", "┻", "─", "┼")
STATUS = ("✔ PASSED", "✘ FAILED")


def extract_summary(file_path):
    """
    Extracts a summary from a given file. This is summary is a table output from the
    inspect command and will be converted into a dictionary.

    Parameters
    ----------
    file_path : str
        The path to the file containing the summary.

    Returns
    -------
    dict
        A dictionary where the keys are the check names and the values are dictionaries
        with 'Status' (bool) and 'Details' (str) of the check.

    Raises
    ------
    FileNotFoundError
        If the file at `file_path` does not exist.
    IOError
        If there is an error reading the file.
    """
    summary, capturing, current_check = {}, False, None

    with open(file_path, "r") as file:
        for line in file:
            if "Inspect Summary" in line:
                capturing = True
                continue

            if capturing:
                if line.startswith("└"):
                    break
                if line.strip().startswith(BORDERS):
                    continue

                if "│" in line:
                    parts = [part.strip() for part in line.strip().split("│")[1:-1]]

                    if len(parts) == 2:
                        key, value = parts
                        if value in STATUS:
                            current_check = key
                            summary[current_check] = {
                                "Status": value == STATUS[0],
                                "Details": "",
                            }
                        elif current_check:
                            summary[current_check][
                                "Details"
                            ] += f" {key} {value}".strip()
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
