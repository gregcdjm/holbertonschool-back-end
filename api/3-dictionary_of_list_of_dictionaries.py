#!/usr/bin/python3
"""Fetch all user data from an api and export it to JSON"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    def fetch_employee_tasks(id, username):
        user_params = {"userId": id}
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos', params=user_params)
        todos = todos.json()

        task_list = []

        for task in todos:
            tsk = {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            }

            task_list.append(tsk)

        return task_list

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    to_export = {}

    for user in users:
        user_tasks = fetch_employee_tasks(user.get('id'), user.get('username'))
        to_export[user.get('id')] = user_tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(to_export, f)
