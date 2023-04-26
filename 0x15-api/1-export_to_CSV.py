#!/usr/bin/python3
"""
Task 0 extended:
    - Export data in CSV format
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Retrieve the user ID from the command-line arguments
    user_id = sys.argv[1]
    # Define the base URL for the REST API
    api_url = "https://jsonplaceholder.typicode.com/"
    # Send a GET request to retrieve the user's information
    user_request = requests.get(api_url + "users/{}".format(user_id)).json()
    # Retrieve the user's username from the response JSON
    username = user_request.get("username")
    # Send a GET request to retrieve all the todos for the user
    todos_request = requests.get(api_url + "todos",
                                 params={"userId": user_id}).json()
    # Open a new CSV file for writing
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        # Create a new CSV writer object
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write each todo's information to the CSV file
        for todo in todos_request:
            writer.writerow([user_id, username,
                             todo.get("completed"), todo.get("title")])
