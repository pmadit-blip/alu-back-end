
# API Assignments

This directory contains Python exercises focused on retrieving and processing data from REST APIs.

## Task 0: Gather Data from an API

**File:** `0-gather_data_from_an_API.py`

This script retrieves employee information and TODO tasks using a REST API.

### Features

- Accepts an employee ID as a command-line argument.
- Retrieves employee details.
- Retrieves the employee's TODO list.
- Counts completed and total tasks.
- Displays the titles of completed tasks.

### Requirements

- Python 3
- urllib
- Internet connection

### Usage

From the repository root, run:

```bash
python3 api/0-gather_data_from_an_API.py 2
```

The script displays the employee's name, completed task count, total task count and completed task titles.

