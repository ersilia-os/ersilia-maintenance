from datetime import datetime

def calculate_expectation(repositories: list):
    """
    Calculates the expected update interval for each repository and recommends a cron period.

    Steps:
    1. Parse and sort update timestamps for each repository.
    2. Calculate intervals (in days) between consecutive updates.
    3. Compute the expectation using equally probable intervals.
    4. Aggregate expectations across all repositories.
    5. Recommend a cron interval based on the overall expectation.

    Parameters:
    repositories (list): A list of dictionaries, each containing:
        - repository_name (str): Name of the repository.
        - update_history (list): List of update timestamps in ISO 8601 format (Z-terminated).

    Returns:
    None: Prints the expectation for each repository and the recommended cron interval.

    Example Output:
    Repository eos4e40 expectation interval: 10.0 days.
    Repository eos0abc expectation interval: 5.00 days.
    Repository eos9f6t expectation interval: 7.50 days.

    Recommended cron interval: 7.50 days
    """

    expectations = []

    for repo in repositories:
        update_dates = [
            datetime.fromisoformat(date.replace("Z", "+00:00")) for date in repo["update_history"]
        ]
        update_dates.sort()  

        if len(update_dates) < 2:
            print(f"Repository {repo['repository_name']} has insufficient data for analysis.")
            continue

        intervals = [
            (update_dates[i] - update_dates[i - 1]).days
            for i in range(1, len(update_dates))
        ]

        probabilities = [1 / len(intervals) for _ in intervals]

        expectation = sum(interval * prob for interval, prob in zip(intervals, probabilities))
        expectations.append(expectation)

        print(
            f"Repository {repo['repository_name']} expectation interval: {expectation:.2f} days."
        )

    if expectations:
        overall_expectation = sum(expectations) / len(expectations)
        print(f"\nRecommended cron interval: {overall_expectation:.2f} days")
    else:
        print("No sufficient data to calculate expectations.")
