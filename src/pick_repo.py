import json
import os
import json
import random
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

REPO_INFO_FILE = Path(__file__).parent.parent / "files" / "repo_info.json"
COMMONF_MODEL_FILE = Path(__file__).parent.parent / "files" / "common_models.json"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def get_repo_to_check(repos: List[Dict[str, str]]) -> Optional[str]:
    """
    Determines which repository should be checked next based on the time it was last checked.

    Parameters
    ----------
    repos : List[Dict[str, str]]
        A list of dictionaries containing repository information. Each dictionary should have
        'repository_name', 'last_updated', and 'most_recent_date_checked' keys.

    Returns
    -------
    Optional[str]
        The name of the repository that should be checked next, or None if no repository needs checking.
    """
    longest_time_ago_repo = None
    longest_time_ago = datetime.now()

    for repo_info in repos:
        last_updated = datetime.strptime(repo_info["last_updated"], DATE_FORMAT)
        last_checked = datetime.strptime(
            repo_info["most_recent_date_checked"], DATE_FORMAT
        )

        if last_updated > last_checked and last_checked < longest_time_ago:
            longest_time_ago_repo = repo_info["repository_name"]
            longest_time_ago = last_checked

    return longest_time_ago_repo


def update_repo_checked_time(repos: List[Dict[str, str]], repo_name: str):
    """
    Updates the 'most_recent_date_checked' field for the specified repository.

    Parameters
    ----------
    repos : List[Dict[str, str]]
        A list of dictionaries containing repository information.
    repo_name : str
        The name of the repository to update.
    """
    for repo_info in repos:
        if repo_info["repository_name"] == repo_name:
            repo_info["most_recent_date_checked"] = datetime.now().strftime(DATE_FORMAT)
            break


def _load_model_ids(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data.get("model_ids", [])


def select_random_models(file_path: str, count: int) -> List[str]:
    """
    Load model IDs from a file and randomly select a specified number of them.

    Parameters:
        file_path (str): Path to the JSON file containing model IDs.
        count (int): Number of model IDs to select.

    Returns:
        List[str]: Randomly selected model IDs.
    """
    model_ids = _load_model_ids(file_path)
    if count > len(model_ids):
        raise ValueError("Count cannot exceed the number of available model IDs.")
    return random.sample(model_ids, count)


def main():
    if not os.path.exists(REPO_INFO_FILE):
        print(f"Error: File '{REPO_INFO_FILE}' does not exist.")
        return

    with open(REPO_INFO_FILE, "r") as json_file:
        repos_data = json.load(json_file)

    repo_to_check = get_repo_to_check(repos_data)

    if repo_to_check:
        update_repo_checked_time(repos_data, repo_to_check)

        with open(REPO_INFO_FILE, "w") as json_file:
            json.dump(repos_data, json_file, indent=4)

        print(repo_to_check)
    else:
        model = select_random_models(COMMONF_MODEL_FILE, 1)[0]
        print(model)


if __name__ == "__main__":
    main()
