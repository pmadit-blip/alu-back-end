#!/usr/bin/python3
"""Exports an employee's TODO list to CSV."""
import csv
import requests
import sys

if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    uid = sys.argv[1]
    user = requests.get("{}/users/{}".format(base, uid)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": uid}).json()
    with open("{}.csv".format(uid), "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            w.writerow([uid, user.get("username"),
                        t.get("completed"), t.get("title")])
