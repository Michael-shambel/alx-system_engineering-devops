#!/usr/bin/python3


import requests
import json

def fetch_user(employee_id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    #url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    resp = requests.get(url)
    return resp.json()

def fetch_todo(employee_id):

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    resp = requests.get(url)
    return resp.json()

def construct_todo_data():
    all_todo_data = {}
    for employee_id in range(1, 11):  # Assuming employee IDs range from 1 to 10
        todo_info = fetch_user(employee_id)
        todo_list = fetch_todo(employee_id)
        todo_data = []
        for task in todo_list:
            todo_data.append({
                "username": todo_info["username"],
                "task": task["title"],
                "completed": task["completed"]
            })
        all_todo_data[str(employee_id)] = todo_data
    return all_todo_data

def export_to_json(data):
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    todo_data = construct_todo_data()
    export_to_json(todo_data)

