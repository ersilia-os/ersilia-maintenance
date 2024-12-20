# Ersilia Maintenance

Welcome to the **Ersilia Maintenance** repository! This project contains automated workflows and scripts to ensure the smooth operation and upkeep of the Ersilia Model Hub.

## General Structure of Maintenance Workflow

The **inspect_model.yml** file defines the GitHub action responsible for running the inspections. The workflow performs several checks on each repository and reports the results. If a check fails, an issue is created with the details.

### Key Components

- **inspect_model.yml**: Defines the GitHub Actions workflow.
- **inspect.sh**: Shell script that runs the inspection process.
- **extract.py**: Processes the inspection results.
- **repo_info.json**: Contains metadata about the repositories.
- **fetch_repos.yml**: GitHub Actions workflow to fetch and update repository data.

## Updating Functions

To add additional checks, update the following files:
1. **publish/test.py**: Create the new check function.
2. **commands/test.py**: Call the new function and store the results.
3. **inspect_model.yml**: Access the results and report them.

## Maintaining Repository List

The **repo_info.json** file contains a list of all repositories in the Ersilia organization. It stores the last time each repository was checked and updated.

### Key Scripts

- **fetch_repos.py**: Initializes `repo_info.json` and uodate with repository data.
- **update_repo_doc.py**: Updates `repo_info.json` with the latest repository information.
- **pick_repo.py**: Selects the next repository to inspect.
- **inspect.sh**: Runs the inspection process for a selected repository.
- **fetch_repos.yml**: Fetches and updates repository data periodically.

### Workflow

#### inspect_model.yml

The `inspect_model.yml` workflow is responsible for inspecting the repositories in the Ersilia Model Hub. It performs the following steps:

1. **Determine Model to Inspect**:
   - If a `MODEL_ID` is provided, it uses that. Otherwise, it runs the `pick_repo.py` script to select a repository.
2. **Run Inspection**:
   - Executes the `inspect.sh` script to run the inspection process.
3. **Process Results**:
   - Runs the `extract.py` script to process the inspection results and create GitHub issues for any failed checks.
4. **Update Repository Information**:
   - Updates the `repo_info.json` file with the current timestamp for the inspected repository.

#### fetch_repos.yml

The `fetch_repos.yml` workflow is responsible for fetching and updating repository data periodically. It performs the following steps:

1. **Fetch Repository Data**:
   - Runs the `make_repo_doc.py` script to initialize the `repo_info.json` file with repository data.
   - Runs the `update_repo_doc.py` script to update the `repo_info.json` file with the latest repository information.
2. **Commit and Push Changes**:
   - Commits the updated `repo_info.json` file and pushes the changes back to the repository.

#### inspect.sh

The `inspect.sh` script is responsible for running the inspection process for a selected repository. It performs the following steps:

1. **Set Up Environment**:
   - Sets up the necessary environment variables and configurations.
2. **Run Inspection Command**:
   - Executes the `ersilia test` command to inspect the repository.
3. **Save Results**:
   - Saves the inspection results to a file named `result.txt`.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.