#!/usr/bin/python3
"""Exports an employee's TODO list to JSON."""
import json
import requests
import sys

if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    uid = sys.argv[1]
    user = requests.get("{}/users/{}".format(base, uid)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": uid}).json()
    data = {uid: [{"task": t.get("title"),
                   "completed": t.get("completed"),
                   "username": user.get("username")} for t in todos]}
    with open("{}.json".format(uid), "w") as f:
        json.dump(data, f)
