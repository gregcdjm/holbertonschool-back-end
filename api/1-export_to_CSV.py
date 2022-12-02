#!/usr/bin/python3
"""Fetch data from an api and export it to CSV"""
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) >= 2:
        employee_id = argv[1]

    if employee_id is None:
        exit()

    userId = {'userId': employee_id}
    id = {'id': employee_id}
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', params=userId)
    todos = todos.json()

    users = requests.get(
        'https://jsonplaceholder.typicode.com/users', params=id)
    users = users.json()

    employee_name = users[0].get('username')
    employee_id = users[0].get('id')
    export_file = '{}.csv'.format(employee_id)

    with open(export_file, 'w') as f:
        for task in todos:
            task_completed = 'True' if task.get('completed') else 'False'

            f.write('"{}","{}","{:s}","{}"\n'.format(
                employee_id,
                employee_name,
                task_completed,
                task.get('title')))
