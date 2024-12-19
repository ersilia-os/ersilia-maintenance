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

### Workflow Steps

1. **Determine Model to Inspect**:
   - Uses either a provided `MODEL_ID` or the `pick_repo.py` script to select a repository.
2. **Update Repository Information**:
   - Updates `repo_info.json` with the current timestamp for the inspected repository.
3. **Run Inspection**:
   - Executes the `ersilia test` command to inspect the repository and saves the results to `result.txt`.
4. **Process Results**:
   - Uses `extract.py` to process the results and create GitHub issues for any failed checks.

## Updating Functions

To add additional checks, update the following files:
1. **publish/inspect.py**: Create the new check function.
2. **commands/inspect.py**: Call the new function and store the results.
3. **inspect_model.yml**: Access the results and report them.

## Maintaining Repository List

The **repo_info.json** file contains a list of all repositories in the Ersilia organization. It stores the last time each repository was checked and updated.

### Key Scripts

- **make_repo_doc.py**: Initializes `repo_info.json` with repository data.
- **update_repo_doc.py**: Updates `repo_info.json` with the latest repository information.
- **pick_repo.py**: Selects the next repository to inspect.
- **inspect.sh**: Runs the inspection process for a selected repository.
- **fetch_repos.yml**: Fetches and updates repository data periodically.



## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

Thank you for using the Ersilia Maintenance repository! We hope this documentation helps you understand and utilize the maintenance workflows effectively.
