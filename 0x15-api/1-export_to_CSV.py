#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports
 it in CSV format
"""
import csv
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
    return todo_info, completed_task


def export_to_csv(employee_id, todo_info, completed_task):
    employee_name = todo_info['username']
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                        "TASK_TITLE"])
        for task in completed_task:
            writer.writerow([employee_id, employee_name, task['completed'],
                            task['title']])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    todo_info, completed_task = display_progress(employee_id)
    export_to_csv(employee_id, todo_info, completed_task)
