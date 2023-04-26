#!/usr/bin/python3

"""
Task 0 extended:
- Export data in JSON format
"""

import json
import requests


if __name__ == "__main__":
    # Define the API URL
    url = "https://jsonplaceholder.typicode.com/"

    # Send a GET request to the API to retrieve all users
    users = requests.get(url + "users").json()

    # Open a file in write mode to store the JSON data
    with open("todo_all_employees.json", "w") as jsonfile:

        # Iterate over each user and retrieve their todos
        user_todos = {}
        for user in users:
            user_id = user.get("id")
            todos = requests.get(url + "todos",
                                 params={"userId": user_id}).json()

            """
            For each todo, create a dictionary with task,
            completion status and username
            """
            todo_list = []
            for todo in todos:
                todo_dict = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
                }
                todo_list.append(todo_dict)

            # Add the list of todos for the current user to the dictionary
            user_todos[user_id] = todo_list

        # Write the final dictionary to the JSON file
        json.dump(user_todos, jsonfile)
