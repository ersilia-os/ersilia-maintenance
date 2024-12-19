import requests
import json
import re
import os
from typing import List, Dict

FILE_PATH = "repo_info.json"
GITHUB_API_URL = "https://api.github.com/orgs/ersilia-os/repos"
HEADERS = {"Accept": "application/vnd.github.v3+json"}
REPO_PATTERN = re.compile(r"^eos[a-zA-Z0-9]{4}$")
DEFAULT_RECENT_CHECK = "2000-01-01T00:00:00Z"


def fetch_repos() -> List[Dict[str, str]]:
    page = 1
    repos = []

    while True:
        params = {"page": page}
        response = requests.get(GITHUB_API_URL, headers=HEADERS, params=params)

        if response.status_code != 200:
            print("Failed to fetch repositories for ersilia.")
            break

        json_response = response.json()
        if not json_response:  # No more repositories to fetch
            break

        for repo in json_response:
            if REPO_PATTERN.match(repo["name"]):
                repos.append(
                    {
                        "repository_name": repo["name"],
                        "last_updated": repo["updated_at"],
                        "most_recent_date_checked": DEFAULT_RECENT_CHECK,
                    }
                )

        page += 1

    print(f"Fetched {len(repos)} repositories.")
    return repos


def load_existing_data(file_path: str) -> List[Dict[str, str]]:
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []


def update_repositories(
    existing_data: List[Dict[str, str]], new_repos: List[Dict[str, str]]
) -> List[Dict[str, str]]:
    for repo in new_repos:
        matching_repo = next(
            (
                item
                for item in existing_data
                if item["repository_name"] == repo["repository_name"]
            ),
            None,
        )

        if not matching_repo:
            print(f"Adding new repository: {repo['repository_name']}")
            existing_data.append(repo)
        else:
            if repo["last_updated"] != matching_repo["last_updated"]:
                print(
                    f"Updating 'last_updated' for {repo['repository_name']} "
                    f"from {matching_repo['last_updated']} to {repo['last_updated']}"
                )
                matching_repo["last_updated"] = repo["last_updated"]
    return existing_data


def save_data_to_file(file_path: str, data: List[Dict[str, str]]):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {file_path}.")


def main():
    existing_data = load_existing_data(FILE_PATH)
    new_repos = fetch_repos()
    updated_data = update_repositories(existing_data, new_repos)
    save_data_to_file(FILE_PATH, updated_data)


if __name__ == "__main__":
    main()
