#!/usr/bin/python3
"""
 Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress
"""
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
    total_task = len(todo_list)
    completed_task = [task for task in todo_list if task['completed']]
    num_completed_task = len(completed_task)
    employee_name = todo_info['name']
    print("Employee {} is done with tasks({}/{})".format(
          employee_name, num_completed_task, total_task))
    for task in completed_task:
        print("\t{}".format(task['title']))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    display_progress(employee_id)
