#!/usr/bin/python3
"""
This script exports all tasks owned by a specific employee to a JSON file.

The script takes a user ID as a command-line argument,
retrieves data about the
tasks assigned to the user from a REST API,
and writes this data to a JSON file.
The file is named "<USER_ID>.json" and contains the following structure:
{
    "USER_ID": [
        {
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS,
            "username": "USERNAME"
        },
        ...
    ]
}

Example usage:
    python3 2-export_to_JSON.py 2
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from command line arguments
    user_id = sys.argv[1]
    
    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    # Fetch the user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch the tasks data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare the tasks data in the required format
    tasks_data = []
    for task in todos_data:
        tasks_data.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })

    # Write data to a JSON file
    filename = f"{user_id}.json"
    with open(filename, mode="w") as json_file:
        json.dump({user_id: tasks_data}, json_file)
