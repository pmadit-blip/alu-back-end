# ALU Back-End

This repository contains backend programming assignments completed as part of the African Leadership University (ALU) software engineering curriculum.

## Project Description

The project focuses on Python programming, working with APIs, handling data, and developing practical backend development skills.

## Directory Structure

```text
alu-back-end/
│
├── api/
│   ├── 0-gather_data_from_an_API.py
│   └── README.md
│
└── README.md
```

## Tasks

### 0. Gather Data from an API

**File:** `api/0-gather_data_from_an_API.py`

A Python script that retrieves employee information and TODO tasks from a REST API.

The script:
- Accepts an employee ID as a command-line argument.
- Retrieves employee information using the REST API.
- Retrieves the employee's TODO list.
- Counts completed and total tasks.
- Displays the employee's name and completed task titles.

## Requirements

- Python 3
- `urllib` module
- Internet connection

## Usage

Run the script from the repository root:

```bash
python3 api/0-gather_data_from_an_API.py 2
```

Replace `2` with the employee ID you want to check.

## Author

ALU Software Engineering Student

