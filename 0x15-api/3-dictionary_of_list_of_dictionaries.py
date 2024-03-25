#!/usr/bin/python3

"""Write a Python script that, using this REST API
[https://jsonplaceholder.typicode.com/], for a given
employee ID, returns information about his/her
TODO list progres
"""

import json
import requests


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com"

    all_users_data = requests.get(f"{base_url}/users")
    all_users_data = all_users_data.json()

    all_users_dict = {}

    for user in all_users_data:
        user_id = user.get("id")
        user_name = user.get("username")
        todo_data = requests.get(f"{base_url}/users/{user_id}/todos")
        todo_data = todo_data.json()

        # Array to hold all tasks for current user
        todo_details = []

        for todo in todo_data:
            todo_completed = todo.get("completed")
            todo_title = todo.get("title")

            # create a dictionary containing some user and task attribute

            new_dict = {"username": user_name, "task": todo_title,
                        "completed": todo_completed}

            # Append single task to the total tasks array
            todo_details.append(new_dict)

        all_users_dict[f"{user_id}"] = todo_details

    # Dump the dictionary of array of dictionary composed
    with open("todo_all_employees.json", "w") as file:
        file.write(json.dumps(all_users_dict))
