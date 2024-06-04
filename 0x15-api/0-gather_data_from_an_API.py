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

    url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit(1)
    user_info = response.json()
    emp_name = user_info.get('name')

    url = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit(1)
    emp_todos = response.json()
    compl_tasks = [task for task in emp_todos if task.get('completed') is True]
    n_todos = len(emp_todos)
    n_compl_tasks = len(compl_tasks)
    print(f'Employee {emp_name} is done with tasks({n_compl_tasks}/{n_todos})')
    [print(f"\t {task.get('title')}") for task in compl_tasks]
