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
    employee_name = todo_info['username']
    csv_file_name = "{}.csv".format(employee_id)
    with open(csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            task_completed_status = "True" if task['completed'] else "False"
            csv_writer.writerow([employee_id, employee_name,
                                 task_completed_status, task['title']])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    display_progress(employee_id)
