#!/usr/bin/python3
"""
This module retrieves and displays the TODO list progress for a given employee
using a REST API. The script accepts an employee ID as a command-line argument
and fetches the employee's name and tasks, showing the number of completed and
total tasks, along with the titles of completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Requirements:
    - requests: Install with `pip install requests`
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress of an employee.

    Args:
        employee_id (int): The ID of the employee to retrieve TODO data for.

    The function retrieves the employee's name and their list of tasks,
    then calculates and displays the number of completed tasks and lists
    the titles of those completed tasks.
    """
    # Define base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user data (employee name)
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    
    # Check if user exists; if not, print an error and exit
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todo list data for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate total tasks and the number of completed tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Print the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    # Ensure an employee ID is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:#!/usr/bin/python3
"""
This script retrieves and displays the TODO list progress for a specified employee
using a REST API. The script takes an employee ID as a command-line argument
and fetches the employee's name and tasks, showing the count of completed and
total tasks, followed by the titles of completed tasks, each correctly formatted.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Requirements:
    - requests: Install with `pip install requests`
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress of an employee.

    Args:
        employee_id (int): The ID of the employee to retrieve TODO data for.

    The function retrieves the employee's name and list of tasks, calculates the
    number of completed and total tasks, and displays them in the required format.
    """
    # Define base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user data for the given employee_id
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    
    # Check if the user exists; if not, print an error and exit
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch the TODO list data for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate total tasks and completed tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    # Display the required information
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            # Convert input to integer and fetch data
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")

        try:
            # Attempt to convert the input argument to an integer
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
