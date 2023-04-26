#!/usr/bin/python3
"""
script that given employee ID, returns information about
his/her TODO list progress using REST API
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Check if the user ID is provided as a command-line argument
    if len(argv) > 1:
        # Retrieve the user ID from the command-line arguments
        user_id = argv[1]
        # Define the base URL for the REST API
        api_url = "https://jsonplaceholder.typicode.com/"
        # Send a GET request to the API endpoint for the specified user
        user_request = requests.get("{}users/{}".format(api_url, user_id))
        # Retrieve the user's name from the response JSON
        user_name = user_request.json().get("name")
        # Check if the user's name exists
        if user_name is not None:
            # Send a GET request to retrieve all the todos for the user
            todos_request = requests.get(
                "{}todos?userId={}".format(api_url, user_id)).json()
            # Count the number of completed tasks
            completed_tasks = [task for task in todos_request if
                               task.get("completed")]
            completed_count = len(completed_tasks)
            # Print a summary message that includes
            # the employee's name and the number of completed tasks
            print("Employee {} is done with tasks({}/{}):".format(
                  user_name, completed_count, len(todos_request)))
            # Print the titles of all completed tasks
            for task in completed_tasks:
                print("\t{}".format(task.get("title")))
