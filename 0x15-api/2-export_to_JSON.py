#!/usr/bin/python3

"""Write a Python script that, using this REST API
[https://jsonplaceholder.typicode.com/], for a given
employee ID, returns information about his/her
TODO list progres
"""
import json
import requests
from sys import argv


if __name__ == "__main__" and len(argv) > 1:
    USER_ID = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_data = requests.get(f"{base_url}/users/{USER_ID}")
    todo_data = requests.get(f"{base_url}/users/{USER_ID}/todos")

    user_data = user_data.json()
    todo_data = todo_data.json()

    # Create string to be written to csv file
    todo_details = []

    for todo in todo_data:
        user_name = user_data.get("username")
        todo_completed = todo.get("completed")
        todo_title = todo.get("title")

        new_dict = {"task": todo_title, "completed": todo_completed,
                    "username": user_name}

        todo_details.append(new_dict)

    # Write composted todos in the array into a file
    with open(f"{USER_ID}.json", "w") as file:
        file.write(json.dumps({f"{USER_ID}": todo_details}))
