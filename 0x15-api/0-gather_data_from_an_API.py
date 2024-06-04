#!/usr/bin/python3
"""
uses a RESTAPI 'https://jsonplaceholder.typicode.com/' for a given employee ID,
returns information about his/her TODO list progress.
"""
import sys
import requests

if len(sys.argv) != 2:
    sys.exit(1)

emp_id = sys.argv[1]

r = requests.get(f'https://jsonplaceholder.typicode.com/users/{emp_id}')
if r.status_code != 200:
    sys.exit(1)
user_info = r.json()
emp_name = user_info.get('name')

r = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')
if r.status_code != 200:
    sys.exit(1)
emp_todos = r.json()
compl_tasks = [task for task in emp_todos if task.get('completed')]
num_todos = len(emp_todos)
num_compl_tasks = len(compl_tasks)
print(f'Employee {emp_name} is done with tasks({num_compl_tasks}/{num_todos})')
[print(f"\t {task.get('title')}") for task in compl_tasks]
