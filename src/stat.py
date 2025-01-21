from datetime import datetime


def calculate_expectation(repositories: list, safety_factor: float = 3.5):
    """
    Calculate the expected interval for checking each repository using weighted probabilities
    based on update frequency. Recommends an adjusted cron interval for GitHub Actions,
    incorporating a safety factor to ensure repositories are not missed.

    Parameters
    ----------
    repositories : list of dict
        A list of dictionaries where each dictionary contains:
            - repository_name : str
                Name of the repository.
            - last_updated : str
                ISO 8601 timestamp of the last update (e.g., "2024-05-08T11:50:32Z").
            - most_recent_date_checked : str
                ISO 8601 timestamp of the most recent check.

    safety_factor : float, optional, default=3.5
        A multiplicative factor applied to the final recommended interval to add uncertainty
        and ensure repositories are checked slightly more frequently than expected.

    Returns
    -------
    None
        Prints the interval, weight, and adjusted cron interval for all repositories,
        along with the final recommended cron interval.

    Notes
    -----
    The calculation proceeds as follows:
    1. Parse the timestamps (`last_updated` and `most_recent_date_checked`) for each repository.
    2. Compute the interval between the two timestamps in days.
    3. Assign weights inversely proportional to the interval (frequent updates -> higher weight).
    4. Compute a weighted average of intervals to derive the overall expectation.
    5. Adjust the expectation with the safety factor to recommend a safer cron interval.
    """

    expectations = []
    weights = []

    for repo in repositories:
        try:
            last_updated = datetime.fromisoformat(
                repo["last_updated"].replace("Z", "+00:00")
            )
            most_recent_date_checked = datetime.fromisoformat(
                repo["most_recent_date_checked"].replace("Z", "+00:00")
            )

            interval = (most_recent_date_checked - last_updated).days

            if interval > 0:
                weight = 1 / interval
                weights.append(weight)
                expectations.append(interval * weight)

                print(
                    f"Repository {repo['repository_name']} interval: {interval} days, weight: {weight:.4f}"
                )
            else:
                print(
                    f"Repository {repo['repository_name']} has invalid interval: {interval} days."
                )

        except Exception as e:
            print(f"Error processing repository {repo['repository_name']}: {e}")
            continue

    if expectations and weights:
        overall_expectation = sum(expectations) / sum(weights)

        adjusted_expectation = overall_expectation / safety_factor

        print(f"\nWeighted average expectation: {overall_expectation:.2f} days")
        print(
            f"Recommended cron interval (with safety factor {safety_factor}): {adjusted_expectation:.2f} days"
        )
    else:
        print("No sufficient data to calculate expectations.")


if __name__ == "__main__":
    import json

    with open("files/repo_info.json") as f:
        repositories = json.load(f)
    calculate_expectation(repositories)
