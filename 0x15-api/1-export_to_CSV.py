#!/usr/bin/python3

"""Write a Python script that, using this REST API
[https://jsonplaceholder.typicode.com/], for a given
employee ID, returns information about his/her
TODO list progres
"""

from http.client import HTTPResponse
import requests
from sys import argv


if __name__ == "__main__" and len(argv) > 1:
    USER_ID = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_data = requests.get(f"{base_url}/users/{USER_ID}")
    todo_data = requests.get(f"{base_url}/users/{USER_ID}/todos")

    user_data = user_data.json()
    todo_data = todo_data.json()

    # num_of_tasks = len(todo_data)
    # completed_tasks = len([cmpl for cmpl in todo_data
    #                        if cmpl.get("completed")])

    # # Print formatted output as on task
    # print("Employee {} is done with tasks({}/{}):"
    #       .format(user_data.get("name", ""), completed_tasks, num_of_tasks))

    # [print("\t {}".format(task["title"]))
    #  for task in todo_data if task.get("completed")]

    # Create string to be written to csv file
    todo_details = []

    for todo in todo_data:
        user_id = user_data.get("id")
        user_name = user_data.get("username")
        todo_completed = todo.get("completed")
        todo_title = todo.get("title")

        new_str = '"{}","{}","{}","{}"\n'\
            .format(user_id, user_name, todo_completed, todo_title)

        todo_details.append(new_str)

    # Write composted todos in the array into a file
    with open(f"{user_id}.csv", "w") as file:
        for todo in todo_details:
            file.write(todo)
