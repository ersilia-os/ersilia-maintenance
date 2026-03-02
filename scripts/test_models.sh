#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PICKED_FILE="${ROOT_DIR}/files/picked_weekly.json"
REPO_INFO_FILE="${ROOT_DIR}/files/repo_info.json"
RESULTS_LOG="${ROOT_DIR}/files/weekly_test_results.txt"

REPORTS_DIR="${ROOT_DIR}/reports"
SUMMARY_TXT="${REPORTS_DIR}/weekly_test_summary.txt"
SUMMARY_MD="${REPORTS_DIR}/weekly_model_testing.md"

# Files tracking per-run state (ephemeral, not committed)
FAILED_MODELS_FILE="${ROOT_DIR}/files/failed_models.txt"
TESTED_MODELS_FILE="${ROOT_DIR}/files/tested_models.txt"
ISSUES_DIR="${ROOT_DIR}/files/issue_bodies"

mkdir -p "${REPORTS_DIR}" "${ISSUES_DIR}"

# Always run from repo root so test JSONs are predictable
cd "${ROOT_DIR}"

# Allow opting out of cleanup for local debugging:
TEST_JSON_CLEANUP="${TEST_JSON_CLEANUP:-1}"

# -----------------------------
# Helpers
# -----------------------------

get_picked_models() {
  if [[ ! -f "${PICKED_FILE}" ]]; then
    echo "ERROR: picked_weekly.json not found at ${PICKED_FILE}" >&2
    exit 1
  fi

  jq -r '.[] | .repository_name | select(. != null and . != "")' "${PICKED_FILE}"
}

get_slug_for_repo() {
  local repo_name="$1"
  jq -r --arg rn "${repo_name}" '
    map(select(.repository_name == $rn) | .slug)[0] // ""
  ' "${PICKED_FILE}"
}

update_json_last_test_date() {
  local repo_name="$1"
  local current_time
  current_time="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"

  echo "Updating last_test_date for repository: ${repo_name}"

  jq --arg rn "${repo_name}" --arg ts "${current_time}" '
    map(
      if .repository_name == $rn
      then .last_test_date = $ts
      else .
      end
    )
  ' "${REPO_INFO_FILE}" > "${REPO_INFO_FILE}.tmp"

  mv "${REPO_INFO_FILE}.tmp" "${REPO_INFO_FILE}"
}

update_json_last_test_outcome() {
  local repo_name="$1"
  local outcome="$2" # Expected: "success" or "failed"

  echo "Updating last_test_outcome for repository: ${repo_name} to ${outcome}"

  jq --arg rn "${repo_name}" --arg outcome "${outcome}" '
    map(
      if .repository_name == $rn
      then .last_test_outcome = $outcome
      else .
      end
    )
  ' "${REPO_INFO_FILE}" > "${REPO_INFO_FILE}.tmp"

  mv "${REPO_INFO_FILE}.tmp" "${REPO_INFO_FILE}"
}

# Sets the status field in repo_info.json for the given repo.
update_json_status() {
  local repo_name="$1"
  local new_status="$2"

  echo "Updating status for repository: ${repo_name} to '${new_status}'"

  jq --arg rn "${repo_name}" --arg status "${new_status}" '
    map(
      if .repository_name == $rn
      then .status = $status
      else .
      end
    )
  ' "${REPO_INFO_FILE}" > "${REPO_INFO_FILE}.tmp"

  mv "${REPO_INFO_FILE}.tmp" "${REPO_INFO_FILE}"
}

commit_and_push() {
  echo "Skipping git commit & push (local mode)."
  # For CI:
  # git config --local user.email "ersilia-bot@users.noreply.github.com"
  # git config --local user.name "ersilia-bot"
  # git add files/repo_info.json files/weekly_test_results.txt reports/
  # git commit -m "Update weekly model test results"
  # git push
}

MODEL_HAS_FAILURE=false
# Accumulated test-result lines for the current model (reset each iteration).
MODEL_TEST_LINES=""

check_results() {
  local category="$1"
  local error_msg_prefix="$2"

  local keys
  keys=$(echo "${results_json}" \
    | jq -r ".[\"${category}\"] // {} | keys[]?" || true)

  if [[ -z "${keys}" ]]; then
    return 0
  fi

  for key in ${keys}; do
    local raw
    raw=$(echo "${results_json}" | jq -r ".[\"${category}\"][\"${key}\"]")

    case "${raw}" in
      true)
        echo "✅ ${category} passed: ${key}"
        echo "✅ [${MODEL_ID}] ${category}: ${key}" >> "${SUMMARY_TXT}"
        MODEL_TEST_LINES+="✅ [${MODEL_ID}] ${category}: ${key}"$'\n'
        ;;
      false)
        MODEL_HAS_FAILURE=true

        local title="🚨 Model ${MODEL_ID} ${category} issue 🚨"
        local body="${error_msg_prefix} '${key}'."

        if [[ -n "${GITHUB_SERVER_URL:-}" && -n "${GITHUB_REPOSITORY:-}" && -n "${GITHUB_RUN_ID:-}" ]]; then
          body+=" Action: ${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID}"
        fi

        echo "${title}"
        echo "${body}"
        echo "🚨 [${MODEL_ID}] ${category}: ${key}" >> "${SUMMARY_TXT}"
        MODEL_TEST_LINES+="🚨 [${MODEL_ID}] ${category}: ${key}"$'\n'
        ;;
      *)
        echo "ℹ️ ${category} metric: ${key} = ${raw}"
        echo "ℹ️ [${MODEL_ID}] ${category}: ${key} = ${raw}" >> "${SUMMARY_TXT}"
        MODEL_TEST_LINES+="ℹ️ [${MODEL_ID}] ${category}: ${key} = ${raw}"$'\n'
        ;;
    esac
  done
}

init_markdown_report() {
  local today
  today="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"

  # Important: unquoted EOF, but backticks are escaped so no command substitution;
  # ${today} is expanded as intended.
  cat > "${SUMMARY_MD}" <<EOF
# 🧪 Weekly Model Testing Report
---

**🗓️ Date:** ${today}

This report summarizes the results of the **weekly shallow tests** run with the \`ersilia\` CLI on the selected repositories from \`picked_weekly.json\`.

Each model has been tested using:

\`\`\`bash
ersilia fetch <repository_name> --from_github
ersilia test <repository_name> --shallow --from_github
\`\`\`

### 📋 Status Legend
- ✅ **Passed:** All checks completed successfully.
- 🚨 **Failed:** One or more checks failed, or the test did not complete.

🔎 For detailed test outputs, see the file: \`reports/weekly_test_summary.txt\`.

---

### 📊 Test Results

| 🧬 repository_name | 🪪 slug | 🧭 test | ⏰ test_date |
|--------------------|---------|---------|--------------|
EOF
}

append_model_to_markdown() {
  local repo_name="$1"
  local slug="$2"
  local status_symbol="$3"
  local test_date
  test_date="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"

  if [[ -z "${slug}" || "${slug}" == "null" ]]; then
    slug="-"
  fi

  echo "| ${repo_name} | ${slug} | ${status_symbol} | ${test_date} |" >> "${SUMMARY_MD}"
}

# Write the issue body markdown file for a failed model.
write_issue_body() {
  local model_id="$1"
  local test_lines="$2"
  local today
  today="$(date -u +'%Y-%m-%d')"

  local body_file="${ISSUES_DIR}/${model_id}.md"

  {
    echo "## Failed weekly maintenance tests"
    echo ""
    echo "The following checks were run on \`${today}\` for model \`${model_id}\`:"
    echo ""
    printf '%s' "${test_lines}"
    if [[ -n "${GITHUB_SERVER_URL:-}" && -n "${GITHUB_REPOSITORY:-}" && -n "${GITHUB_RUN_ID:-}" ]]; then
      echo ""
      echo "---"
      echo "For detailed logs, see the [workflow run](${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID})."
    fi
  } > "${body_file}"

  echo "Issue body written to: ${body_file}"
}

# -----------------------------
# Main
# -----------------------------

: > "${RESULTS_LOG}"
: > "${SUMMARY_TXT}"
: > "${FAILED_MODELS_FILE}"
: > "${TESTED_MODELS_FILE}"
init_markdown_report

models_to_test=$(get_picked_models || true)

if [[ -z "${models_to_test}" ]]; then
  echo "No models found in picked_weekly.json. Exiting."
  exit 0
fi

for MODEL_ID in ${models_to_test}; do
  echo "==============================================" | tee -a "${SUMMARY_TXT}"
  echo "Testing model: ${MODEL_ID}" | tee -a "${SUMMARY_TXT}"
  echo "==============================================" | tee -a "${SUMMARY_TXT}"

  MODEL_HAS_FAILURE=false
  MODEL_TEST_LINES=""
  slug=$(get_slug_for_repo "${MODEL_ID}")

  # Fetch & test
  set +e
  ersilia -v fetch "${MODEL_ID}" --from_github | tee -a "${RESULTS_LOG}"
  fetch_exit=$?

  ersilia test "${MODEL_ID}" --shallow --from_github | tee -a "${RESULTS_LOG}"
  test_exit=$?
  set -e

  if [[ ${fetch_exit} -ne 0 || ${test_exit} -ne 0 ]]; then
    echo "ersilia fetch/test failed for ${MODEL_ID} (fetch_exit=${fetch_exit}, test_exit=${test_exit})." | tee -a "${RESULTS_LOG}" | tee -a "${SUMMARY_TXT}"
    MODEL_HAS_FAILURE=true
    MODEL_TEST_LINES+="🚨 [${MODEL_ID}] ersilia: fetch/test command failed (fetch_exit=${fetch_exit}, test_exit=${test_exit})"$'\n'
  fi

  report_json="${MODEL_ID}-test.json"

  if [[ ! -f "${report_json}" ]]; then
    echo "WARNING: Test report JSON not found for ${MODEL_ID}: ${report_json}" | tee -a "${RESULTS_LOG}" | tee -a "${SUMMARY_TXT}"
    MODEL_HAS_FAILURE=true
    MODEL_TEST_LINES+="🚨 [${MODEL_ID}] ersilia: test report JSON not found"$'\n'
  else
    echo "Parsing report with extract.py for ${MODEL_ID}..."
    results_json=$(python3 "${ROOT_DIR}/src/extract.py" "${report_json}")

    if [[ -z "${results_json}" ]]; then
      echo "WARNING: extract.py returned empty results for ${MODEL_ID}." | tee -a "${RESULTS_LOG}" | tee -a "${SUMMARY_TXT}"
      MODEL_HAS_FAILURE=true
      MODEL_TEST_LINES+="🚨 [${MODEL_ID}] ersilia: extract.py returned empty results"$'\n'
    else
      check_results "metadata_checks" "Metadata check failed for key"
      check_results "model_file_checks" "Model file check failed for file"
      check_results "file_validity_check" "File validity check failed for"
      check_results "model_size_check" "Model size check failed for"
      check_results "model_run_check" "Model run check failed for"
      check_results "async_model_run_check" "Async model run check failed for"
      check_results "input_output_check" "Input/output validation failed for"
      check_results "model_output_consistency_check" "Output consistency issue for"
      check_results "consistency_summary_between_ersilia_and_bash_execution_outputs" "Consistency summary issue for"
    fi
  fi

  update_json_last_test_date "${MODEL_ID}"

  if [[ "${MODEL_HAS_FAILURE}" == true ]]; then
    append_model_to_markdown "${MODEL_ID}" "${slug}" "🚨"
    update_json_last_test_outcome "${MODEL_ID}" "failed"
    update_json_status "${MODEL_ID}" "In maintenance"
    echo "${MODEL_ID}" >> "${FAILED_MODELS_FILE}"
    write_issue_body "${MODEL_ID}" "${MODEL_TEST_LINES}"
  else
    append_model_to_markdown "${MODEL_ID}" "${slug}" "✅"
    update_json_last_test_outcome "${MODEL_ID}" "success"
  fi

  echo "${MODEL_ID}" >> "${TESTED_MODELS_FILE}"

  # Cleanup test JSON file unless explicitly disabled
  if [[ "${TEST_JSON_CLEANUP}" -eq 1 && -n "${report_json:-}" && -f "${report_json}" ]]; then
    rm -f "${report_json}"
  fi

done

# commit_and_push  # enable in CI if desired

echo "Weekly tests completed."
echo "Raw log: ${RESULTS_LOG}"
echo "Condensed summary: ${SUMMARY_TXT}"
echo "Markdown report: ${SUMMARY_MD}"
echo "Failed models: ${FAILED_MODELS_FILE}"
echo "Tested models: ${TESTED_MODELS_FILE}"
