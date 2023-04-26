#!/usr/bin/python3
"""
Task 0 extended:
    - Export data in JSON format
"""

import json
import requests
import sys


if __name__ == "__main__":
    # Retrieve the user ID from the command-line arguments
    user_id = sys.argv[1]
    # Define the base URL for the REST API
    url = "https://jsonplaceholder.typicode.com/"
    # Send a GET request to retrieve the user's information
    user_request = requests.get(url + "users/{}".format(user_id)).json()
    # Retrieve the user's username from the response JSON
    username = user_request.get("username")
    # Send a GET request to retrieve all the todos for the user
    todos_request = requests.get(url + "todos", params={"userId": user_id}).json()
    # Open a new JSON file for writing
    with open("{}.json".format(user_id), "w") as jsonfile:
        # Create a dictionary to store the user's information and todos
        user_dict = {}
        # Create a list to store the todos
        todos_list = []
        # Add each todo to the list
        for todo in todos_request:
            todo_dict = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            todos_list.append(todo_dict)
        # Add the user's information and todos to the dictionary
        user_dict[user_id] = todos_list
        # Write the dictionary to the JSON file
        json.dump(user_dict, jsonfile)
