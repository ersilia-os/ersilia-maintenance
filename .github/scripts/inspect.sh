#!/bin/bash

# =================================================
# Shell Script to Inspect a Model and Report Issues
# =================================================
# This script performs the following:
# 1. Determine the model to inspect using MODEL_ID or run 'pick_repo.py' script.
# 2. Update 'repo_info.json' with the current timestamp for the model inspected.
# 3. Execute 'ersilia test' to inspect the model and save results to 'result.txt'.
# 4. Process results using 'extract.py' to extract inspection details from output.
# 5. Create GitHub issues for failed checks based on inspection results obtained.

if [ -n "$MODEL_ID" ]; then
  echo "Using input model ID: $MODEL_ID"
else
  echo "Getting next model from Python script."
  MODEL_ID=$(python3 src/pick_repo.py)
fi

mkdir -p files
if [ ! -f files/repo_info.json ]; then
  echo "[]" > files/repo_info.json
fi

jq --arg repo_name "$MODEL_ID" \
   --arg current_time "$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
   'map(if .repository_name == $repo_name then .most_recent_date_checked = $current_time else . end)' \
   files/repo_info.json > temp_repo_info.json
mv temp_repo_info.json files/repo_info.json

git config --local user.email "ersilia-bot@users.noreply.github.com"
git config --local user.name "ersilia-bot"
git add files/repo_info.json
git commit -m "Edited the JSON file"
git push

echo "Running ersilia test for model ID: $MODEL_ID..."
ersilia test "$MODEL_ID" -d "$MODEL_ID" --inspect --remote > result.txt

if [ ! -f "result.txt" ]; then
    echo "Error: Failed to generate result.txt."
    exit 1
fi

echo "Processing the result with extract.py..."
results_json=$(python3 src/extract.py result.txt)

echo "Inspection Results JSON:"
echo "$results_json"

echo "$results_json" | jq -c 'to_entries[]' | while read -r item; do
    key=$(echo "$item" | jq -r '.key')  
    status=$(echo "$item" | jq -r '.value.Status')
    details=$(echo "$item" | jq -r '.value.Details') 

    if [ "$status" = "false" ]; then
        title="🚨 Model $MODEL_ID $key Issue 🚨"
        body="Details: $details<br><br>Action: $GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID"

        exists=$(gh issue list --repo "$REPO_OWNER/$REPO_NAME" --search "$title in:title" | grep -q "$title")
        if [ -z "$exists" ]; then
            gh issue create --repo "$REPO_OWNER/$REPO_NAME" --title "$title" --body "$body"
        else
            echo "Issue already exists: $title"
        fi
    else
        echo "✅ Check Passed: $key"
    fi
done

echo "Process completed successfully."
