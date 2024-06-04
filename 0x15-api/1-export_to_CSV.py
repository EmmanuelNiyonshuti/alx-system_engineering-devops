#!/usr/bin/python3
"""
uses a RESTAPI 'https://jsonplaceholder.typicode.com/' for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
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
    csv_data = []
    for todo in emp_todos:
        task_title = todo.get('title')
        task_done = todo.get('completed')
        csv_data.append([emp_id, user_name, task_done, task_title])

    csv_file = "{}.csv".format(emp_id)
    with open(csv_file, 'w', newline="") as csv_f:
        writer = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)
