#!/usr/bin/python3
"""
script that given employee ID, returns information about
his/her TODO list progress using REST API
"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    username = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    completed = []
    for task in todos:
        if task.get("completed") is True:
            completed.append(task.get("title"))

    completed_tasks = len(completed)
    total_tasks = len(todos)
    print("Employee {} is done with tasks({}/{}):".format(
          username.get("name"), completed_tasks, total_tasks))

    for task_title in completed:
        print("\t {}".format(task_title))
