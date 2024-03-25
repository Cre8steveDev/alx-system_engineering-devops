#!/usr/bin/python3

"""Write a Python script that, using this REST API
[https://jsonplaceholder.typicode.com/], for a given
employee ID, returns information about his/her
TODO list progres
"""

from http.client import HTTPResponse
import requests
from sys import argv

USER_ID = argv[1]
base_url = "https://jsonplaceholder.typicode.com"

user_data = requests.get(f"{base_url}/users/{USER_ID}")
todo_data = requests.get(f"{base_url}/users/{USER_ID}/todos")

user_data = user_data.json()
todo_data = todo_data.json()

num_of_tasks = len(todo_data)
completed_tasks = len([cmpl for cmpl in todo_data
                       if cmpl["completed"]])

# Print formatted output as on task
print("Employee {} is done with tasks({}/{}):"
      .format(user_data.get("name", ""), completed_tasks, num_of_tasks))

[print("\t {}".format(task["title"])) for task in todo_data
 if task["completed"]]
