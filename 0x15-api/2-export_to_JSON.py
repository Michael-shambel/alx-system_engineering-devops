#!/usr/bin/python3
"""
xtend your Python script to export data in the JSON format.
"""
import json
import requests
import sys


def fetch_user(employee_id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    resp = requests.get(url)
    return resp.json()


def fetch_todo(employee_id):
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
               employee_id)
    resp = requests.get(url)
    return resp.json()


def export_to_json(employee_id, todo_info, todo_list):
    employee_name = todo_info['name']
    tasks = [{'task': task['title'], 'completed': task['completed'],
             'username': employee_name} for task in todo_list]
    data = {str(employee_id): tasks}
    filename = "{}.json".format(employee_id)
    with open(filename, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    todo_info = fetch_user(employee_id)
    todo_list = fetch_todo(employee_id)
    export_to_json(employee_id, todo_info, todo_list)
