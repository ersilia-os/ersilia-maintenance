#!/bin/bash

# =================================================
# Shell Script to Inspect a Model and Report Issues
# =================================================
# This script performs the following:
# 1. Determine the model to inspect using MODEL_ID or run 'pick_repo.py' script.
# 2. Update 'repo_info.json' with the current timestamp for the model inspected.
# 3. Execute 'ersilia test' to inspect the model and save results to 'result.txt'.
# 4. Read results using 'extract.py' to extract test command checks details.
# 5. Create GitHub issues for failed checks based on inspection results obtained.


set -e

get_model_id() {
  if [ -n "$MODEL_ID" ]; then
    echo "Using input model ID: $MODEL_ID"
  else
    echo "Getting next model from Python script."
    MODEL_ID=$(python3 ./src/pick_repo.py)
  fi
}

update_json() {
  echo "Updating json file [repo_info]."
  jq --arg repo_name "$MODEL_ID" \
     --arg current_time "$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
     'map(if .repository_name == $repo_name then .most_recent_date_checked = $current_time else . end)' \
     ./files/repo_info.json > temp_repo_info.json
  mv temp_repo_info.json ./files/repo_info.json
  echo "Moving json file [repo_info]."

}

commit_and_push() {
  echo "Commenting and pushing Updated json file [repo_info]."
  git config --local user.email "ersilia-bot@users.noreply.github.com"
  git config --local user.name "ersilia-bot"
  git add .
  git commit -m "Edited the JSON file"
  git push
}
create_github_issue() {
  echo "Creating github issue."
  local title="$1"
  local body="$2"
  if ! gh issue list --repo "$REPO_OWNER/$REPO_NAME" --search "$title in:title" | grep -q "$title"; then
    gh issue create --repo "$REPO_OWNER/$REPO_NAME" --title "$title" --body "$body"
  else
    echo "Issue already exists: $title"
  fi
}

check_results() {
  local category="$1"
  local json_key="$2"
  local error_msg="$3"

  for key in $(echo "$results_json" | jq -r ".$category | keys[]"); do
    status=$(echo "$results_json" | jq -r ".$category[\"$key\"]")
    if [ "$status" = "false" ]; then
      title="🚨 Model $MODEL_ID $category Issue 🚨"
      body="$error_msg '$key'. Action: $GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID"
      create_github_issue "$title" "$body"
    else
      echo "✅ $category Passed: $key"
    fi
  done
}

get_model_id
update_json
commit_and_push

echo "Running ersilia test for model ID: $MODEL_ID..."
ersilia -v fetch "$MODEL_ID" --from_dockerhub --version dev-amd64
ersilia test "$MODEL_ID" --shallow --from_github

echo "Reading reports with extract.py..."
results_json=$(python3 ./src/extract.py "$MODEL_ID-test.json")

check_results "metadata_checks" "Metadata checks" "Key"
check_results "model_file_checks" "Model File Checks" "File"
check_results "file_validity_check" "File validity check [dependency]" "File"
check_results "model_size_check" "Model Size Check" "Size"
check_results "model_run_check" "ModelRun Check" "Run Check"
check_results "input_output_check" "Content validation Check" "Content validation Check"
check_results "model_output_consistency_check" "consistency_summary" "Key"
check_results "model_output_content_validation_summary" "model_output_content_validation_summary" "Invalid file content"
