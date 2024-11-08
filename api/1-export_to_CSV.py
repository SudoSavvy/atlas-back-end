#!/usr/bin/python3
"""
This script exports all tasks owned by a specific employee to a CSV file.

The script takes a user ID as a command-line argument, retrieves data about the
tasks assigned to the user from a REST API, and writes this data to a CSV file.
The file is named "<USER_ID>.csv" and contains the following columns:
- USER_ID
- USERNAME
- TASK_COMPLETED_STATUS
- TASK_TITLE

Example usage:
    python3 1-export_to_CSV.py 2
"""

import csv
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

    # Open a CSV file for writing
    filename = f"{user_id}.csv"
    with open(filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write each task to the CSV file
        for task in todos_data:
            csv_writer.writerow([
                user_id,
                username,
                task["completed"],
                task["title"]
            ])
