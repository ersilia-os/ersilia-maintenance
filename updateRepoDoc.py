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
    print(len(repos))
    return(repos)



file_path = "repo_info.json"
with open(file_path, 'r') as json_file:
        data = json.load(json_file)
repositories = getRepos()
for repo in repositories:
    matching_elements = [item for item in data if item["repository_name"] == repo["repository_name"]]
    if not matching_elements:
        print(f"Adding new repository: {repo['repository_name']}")
        data.append(repo)
    else:
        print(f"Found existing repository: {repo['repository_name']}")
        current = matching_elements[0]
        if repo["last_updated"] != current["last_updated"]:
            print(f"Updating last_updated for {repo['repository_name']} from {current['last_updated']} to {repo['last_updated']}")
            current["last_updated"] = repo["last_updated"]

with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
