import requests
import json
from datetime import datetime
import re
import os

def getRepos():
    page = 1
    repos = []
    repo_pattern = re.compile(r'^eos[a-zA-Z0-9]{4}$')
    while True:
        params = {"page": page}
        url = f"https://api.github.com/orgs/ersilia-os/repos"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(url, headers=headers, params=params)
        default_recent_check = "2000-01-01T00:00:00Z"
        if response.status_code == 200:
            if len(response.json()) == 0:
                break  # No more repositories to fetch
            for repo in response.json():
                if repo_pattern.match(repo["name"]):
                    name = repo["name"]
                    last_updated = repo["updated_at"]
                    repos.append({
                        "repository_name": name,
                        "last_updated": last_updated,
                        "most_recent_date_checked": default_recent_check  # Initial value
                    })
            page += 1
        else:
            print(f"Failed to fetch repositories for ersilia.")
            break
    print(repos)
    return(repos)



file_path = "repo_info.json"

if not os.path.exists(file_path):
    print("Making JSON")
    repositories = getRepos()
    with open(file_path, 'w') as json_file:
        json.dump(repositories, json_file, indent=4)
else:
    print("JSON already exists")

