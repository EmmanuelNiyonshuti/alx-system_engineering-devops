#!/usr/bin/python3
"""
uses a RESTAPI 'https://jsonplaceholder.typicode.com/' for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(1)

    emp_id = sys.argv[1]

    users_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    response = requests.get(users_url)
    if response.status_code != 200:
        sys.exit(1)
    user_info = response.json()
    emp_name = user_info.get('name')
    user_name = user_info.get('username')
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'
    response = requests.get(todos_url)
    if response.status_code != 200:
        sys.exit(1)
    emp_todos = response.json()
    todos_list = []
    for todo in emp_todos:
        todos_list.append({
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user_name
        })
    todos_dict = {emp_id: todos_list}

    json_file = "{}.json".format(emp_id)
    with open(json_file, 'w') as json_f:
        json.dump(todos_dict, json_f)
