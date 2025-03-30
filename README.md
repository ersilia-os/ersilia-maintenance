# Ersilia Maintenance

Welcome to the **Ersilia Maintenance** repository! This project provides automated workflows and scripts to ensure the efficient operation of the Ersilia Model Hub. The system performs periodic inspections of models from the hub, identifies issues, and creates GitHub issues when errors are detected.

## Overview of Workflows

### Key Workflows

#### `inspect_model.yml`
This GitHub Actions workflow is responsible for inspecting repositories within the Ersilia Model Hub. It follows these steps:

1. **Determine the Model to Inspect**:
   - Uses the `MODEL_ID` environment variable if provided.
   - If `MODEL_ID` is absent, runs the `pick_repo.py` script to select a repository.

2. **Run Inspection**:
   - Executes the `inspect.sh` script to conduct the inspection process.

3. **Process Results**:
   - Utilizes the `extract.py` script to process the inspection output.
   - Automatically creates GitHub issues for any failed checks.

4. **Update Repository Data**:
   - Updates the `repo_info.json` file with the inspection timestamp.

#### `fetch_repos.yml`
This workflow ensures the repository data is regularly updated. Key steps include:

1. **Fetch Data**:
   - Runs `fetch_repos.py` to initialize or refresh `repo_info.json` with repository metadata.
   - Executes `update_repo_doc.py` to synchronize the latest repository details.

2. **Commit Changes**:
   - Commits and pushes updates to `repo_info.json` back to the repository.

## Key Components

- **`inspect_model.yml`**: Defines the main inspection workflow.
- **`inspect.sh`**: A shell script that runs the inspection process.
- **`extract.py`**: Extract inspection results from a test commands and print dump them, for the `inspect.sh` to be able to process them.
- **`repo_info.json`**: Stores metadata about repositories, including the last inspection timestamp.
- **`fetch_repos.yml`**: Periodically updates repository data.

## Adding New Inspection Checks
To introduce additional checks, modify the following files:

1. **`publish/test.py`**:
   - Implement the new check function here.

2. **`commands/test.py`**:
   - Invoke the new function and store its results.

3. **`inspect_model.yml`**:
   - Update the workflow to utilize the new check results.

## Maintaining Repository Metadata

The `repo_info.json` file tracks the repositories managed by the Ersilia organization. It includes metadata such as the last inspection date and repository status.

### Key Scripts

- **`fetch_repos.py`**:
  - Initializes or updates `repo_info.json` with repository details.

- **`update_repo_doc.py`**:
  - Updates existing entries in `repo_info.json` with the latest information.

- **`pick_repo.py`**:
  - Selects the next repository for inspection. If no models require immediate attention, a random model from `common_files.json` is chosen.

- **`inspect.sh`**:
  - Executes the inspection process for a specified repository.

## Inspection Workflow Details

### Inspection Process (`inspect.sh`)

1. **Environment Setup**:
   - Configures necessary environment variables and dependencies.

2. **Run Inspection**:
   - Executes the `ersilia test` command to inspect the repository. This includes fetching models and performing checks.

3. **Save Results**:
   - Stores results in `result.txt`.
   - Uses `extract.py` to read output JSON report file from the test command which has structure like this:

```json
{
    "model_file_checks": {
        "dockerfile": true,
        "metadata_json": true,
        "model_framework_run_sh": true,
        "src_service_py": true,
        "pack_py": true,
        "readme_md": true,
        "license": true
    },
    ...
}
```

4. **Error Handling**:
   - For checks with a `false` status in each check fields (eg. `model_file_checks`).

## License

This project is licensed under the GNU General Public License v3.0. For details, refer to the [LICENSE](LICENSE) file.
