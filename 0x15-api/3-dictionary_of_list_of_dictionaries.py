#!/usr/bin/python3
""""
uses a RESTAPI 'https://jsonplaceholder.typicode.com/' for a given employee ID,
returns information about his/her TODO list progress.
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
    """ construct a dictionary so that I will get a username"""
    users_dict = {user['id']: user['username'] for user in users_obj}

    todos_r = requests.get(todos_url)
    if todos_r.status_code != 200:
        pass
    todos_obj = todos_r.json()
    todos_list = []
    for todo in todos_obj:
        for i, name in users_dict.items():
            """check if the userId  in todos is the same as id in users
            to get the corresponding username and id.
            """
            if todo.get('userId') == i:
                username = name
                user_id = i
        todos_list.append({
            'username': username,
            'task': todo.get('title'),
            'completed': todo.get('completed')
        })
    todos_dict = {user_id: todos_list}
    with open('todo_all_employees.json', 'w') as json_f:
        json.dump(todos_dict, json_f)
