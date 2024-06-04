#!/usr/bin/python3
"""
uses a RESTAPI 'https://jsonplaceholder.typicode.com/' for a given employee ID,
returns information about his/her TODO list progress.
"""
import sys
import requests

if len(sys.argv) != 2:
    sys.exit(1)

employee_id = sys.argv[1]

user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
if user_response.status_code != 200:
    sys.exit(1)
user_info = user_response.json()
employee_name = user_info.get('name')

todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
if todos_response.status_code != 200:
    sys.exit(1)
employee_todos = todos_response.json()
completed_tasks = [task for task in employee_todos if task.get('completed')]

print(f'Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(employee_todos)})')
[print(f"\t {task.get('title')}") for task in completed_tasks]
