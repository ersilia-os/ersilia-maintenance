import requests
import json
from datetime import datetime
import os

def getRepoToCheck(repos):
    longest_time_ago_repo = None
    longest_time_ago = datetime.now()
    
    for repo_info in repos:
        last_updated = datetime.strptime(repo_info["last_updated"], "%Y-%m-%dT%H:%M:%SZ")
        last_checked = datetime.strptime(repo_info["most_recent_date_checked"], "%Y-%m-%dT%H:%M:%SZ")

        if last_updated > last_checked and last_checked < longest_time_ago:
            longest_time_ago_repo = repo_info["repository_name"]
            longest_time_ago = last_checked

    return longest_time_ago_repo


file_path = "repo_info.json"
    
with open(file_path, 'r') as json_file:
        data = json.load(json_file)

repo = getRepoToCheck(data)

if repo:
    for repo_info in data:
        if repo_info["repository_name"] == repo:
            repo_info["most_recent_date_checked"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    # Update the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    # print(f"The most_recent_date_checked for {repo} has been updated to the current datetime.")
    print(repo)
else:
    print("None")


