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


def display_progress(employee_id):
    todo_info = fetch_user(employee_id)
    todo_list = fetch_todo(employee_id)
    employee_name = todo_info['username']
    json_data = {str(employee_id): [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in todo_list]}
    json_file_name = "{}.json".format(employee_id)

    with open(json_file_name, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    display_progress(employee_id)
