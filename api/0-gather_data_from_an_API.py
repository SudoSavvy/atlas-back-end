#!/usr/bin/python3
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    # Define base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    
    # Check if user exists
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todo list data
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate task progress
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    # Ensure an employee ID was provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
