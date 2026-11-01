#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base}/users/{user_id}").json()
    todos = requests.get(f"{base}/todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([user_id, user.get("username"),
                             t.get("completed"), t.get("title")])
