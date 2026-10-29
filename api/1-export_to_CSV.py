#!/usr/bin/python3
"""Export employee tasks to CSV."""

import csv
import sys
from pathlib import Path

import requests


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(user_url).json()
    username = user.get("username")

    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    tasks = requests.get(tasks_url).json()

    file_path = Path(__file__).resolve().parent / f"{user_id}.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
