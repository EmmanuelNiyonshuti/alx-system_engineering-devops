#!/usr/bin/python3
"""
uses a RESTAPI 'https://jsonplaceholder.typicode.com/' for a given employee ID,
returns information about his/her TODO list progress.
"""
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
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'
    response = requests.get(todos_url)
    if response.status_code != 200:
        sys.exit(1)
    emp_todos = response.json()
    compl_tasks = [task for task in emp_todos if task.get('completed') is True]
    todos_done = len(emp_todos)
    todos_count = len(compl_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, todos_count, todos_done))

    [print(f"\t {task.get('title')}") for task in compl_tasks]
