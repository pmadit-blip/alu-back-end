#!/usr/bin/python3
"""Export employee tasks to CSV."""

import csv
import json
from pathlib import Path
import sys
import urllib.request


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
    tasks_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    )

    with urllib.request.urlopen(user_url) as response:
        user = json.load(response)

    with urllib.request.urlopen(tasks_url) as response:
        tasks = json.load(response)

    file_path = Path(__file__).resolve().parent / f"{user_id}.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([
                user_id,
                user["username"],
                task["completed"],
                task["title"]
            ])

