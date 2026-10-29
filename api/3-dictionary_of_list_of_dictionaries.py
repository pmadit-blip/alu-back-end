#!/usr/bin/python3
"""Exports all employees' TODO lists to JSON."""
import json
import requests

if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(base)).json()
    todos = requests.get("{}/todos".format(base)).json()
    data = {}
    for u in users:
        data[str(u["id"])] = [{"username": u["username"],
                               "task": t["title"],
                               "completed": t["completed"]}
                              for t in todos if t["userId"] == u["id"]]
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
