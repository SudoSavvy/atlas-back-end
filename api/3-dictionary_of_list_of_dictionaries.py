#!/usr/bin/python3

"""
This module provides functionality for exporting task data to JSON format.
It retrieves task records for all users and stores them in a structured 
dictionary format, then writes the data to a JSON file.

The structure of the output is:
{
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", 
        "completed": TASK_COMPLETED_STATUS},
        ...
    ]
}
"""

import json
import requests


def fetch_data():
    # Assuming you're getting the task data from a remote URL or local API
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    return response.json()


def process_data(tasks):
    user_tasks = {}

    # Group tasks by user ID
    for task in tasks:
        user_id = str(task['userId'])
        task_data = {
            "username": task['username'],
            "task": task['title'],
            "completed": task['completed']
        }

        if user_id not in user_tasks:
            user_tasks[user_id] = []
        user_tasks[user_id].append(task_data)

    return user_tasks


def save_to_json(data):
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


def main():
    # Fetch task data
    tasks = fetch_data()

    # Process and group tasks by user
    user_data = process_data(tasks)

    # Save the grouped tasks into a JSON file
    save_to_json(user_data)


if __name__ == "__main__":
    main()
