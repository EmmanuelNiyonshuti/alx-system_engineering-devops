#!/usr/bin/python3
"""
Uses a RESTAPI 'https://jsonplaceholder.typicode.com/' for a given employee ID,
returns information about their TODO list progress.
"""
import json
import requests

if __name__ == "__main__":
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    users_r = requests.get(users_url)
    if users_r.status_code != 200:
        pass
    users_obj = users_r.json()
    users_dict = {user['id']: user['username'] for user in users_obj}

    todos_r = requests.get(todos_url)
    if todos_r.status_code != 200:
        pass
    todos_obj = todos_r.json()

    """Create a dictionary to store tasks for each user ID"""
    todos_dict = {}
    for todo in todos_obj:
        user_id = todo.get('userId')
        username = users_dict.get(user_id)
        task = todo.get('title')
        completed = todo.get('completed')

        if user_id not in todos_dict:
            todos_dict[user_id] = []

        todos_dict[user_id].append({
            'username': username,
            'task': task,
            'completed': completed
        })

    with open('todo_all_employees.json', 'w') as json_f:
        json.dump(todos_dict, json_f)
