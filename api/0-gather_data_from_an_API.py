#!/usr/bin/python3
"""Gather employee TODO progress from a REST API."""

import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    tasks_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    with urllib.request.urlopen(user_url) as response:
        employee = json.load(response)

    with urllib.request.urlopen(tasks_url) as response:
        tasks = json.load(response)

    completed_tasks = [
        task for task in tasks if task["completed"]
    ]

    print(
        f"Employee {employee['name']} is done with tasks"
        f"({len(completed_tasks)}/{len(tasks)}):"
    )

    for task in completed_tasks:
        print(f"\t {task['title']}")
