import requests
import json
import re
import os
from typing import List, Dict
from pathlib import Path

GITHUB_API_URL = "https://api.github.com/orgs/ersilia-os/repos"
HEADERS = {"Accept": "application/vnd.github.v3+json"}
DEFAULT_RECENT_CHECK = "2000-01-01T00:00:00Z"
REPO_PATTERN = re.compile(r"^eos[a-zA-Z0-9]{4}$")
FILE_PATH = Path(__file__).parent.parent / "files" / "repo_info.json"

def fetch_repositories() -> List[Dict[str, str]]:
    """
    Retrieve repositories from the 'ersilia-os' GitHub organization that match 
    a specific pattern.

    This function uses the GitHub API to fetch all repositories under 'ersilia-os', 
    filters them based on the regular expression as in `REPO_PATTERN`, and collects 
    their names, last updated timestamps, and a default recent check date.
    
    Returns
    -------
    List[Dict[str, str]]
        A list of dictionaries containing repository information with keys:
        'repository_name', 'last_updated', and 'most_recent_date_checked'.
    """
    page, repositories = 1, []

    while True:
        try:
            response = requests.get(
                GITHUB_API_URL, headers=HEADERS, params={"page": page}
            )
            response.raise_for_status()
            repos_data = response.json()

            if not repos_data:
                break

            for repo in repos_data:
                if REPO_PATTERN.match(repo["name"]):
                    repositories.append(
                        {
                            "repository_name": repo["name"],
                            "last_updated": repo["updated_at"],
                            "most_recent_date_checked": DEFAULT_RECENT_CHECK,
                        }
                    )
            page += 1

        except requests.RequestException as e:
            print(f"Failed to fetch repositories: {e}")
            break

    return repositories


def update_repository_file(file_path: str, data: List[Dict[str, str]]):
    """
    Save repository data to a JSON file, updating existing entries if necessary.

    Parameters
    ----------
    file_path : str
        The path to the JSON file where repository data will be saved.
    data : List[Dict[str, str]]
        The repository data to save.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            existing_data = json.load(json_file)
        current_repos = {repo["repository_name"]: repo for repo in existing_data}
    else:
        current_repos = {}

    for repo in data:
        repo_name = repo["repository_name"]
        if repo_name in current_repos:
            if repo["last_updated"] > current_repos[repo_name]["last_updated"]:
                current_repos[repo_name]["last_updated"] = repo["last_updated"]
        else:
            current_repos[repo_name] = repo

    with open(file_path, "w") as json_file:
        json.dump(list(current_repos.values()), json_file, indent=4)
    print(f"Repository data saved to {file_path}")


def main():
    print("Fetching repository data...")
    repositories = fetch_repositories()
    update_repository_file(FILE_PATH, repositories)

if __name__ == "__main__":
    main()
