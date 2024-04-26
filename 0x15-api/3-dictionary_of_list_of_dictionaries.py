#!/usr/bin/python3


import requests
import json
import sys

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    todo_all_employees = {}
    for user in users:
        user_id = str(user["id"])
        user_name = user["username"]
        todo_all_employees[user_id] = []

        for todo in todos:
            if todo["userId"] == int(user_id):
                todo_all_employees[user_id].append({
                    "username": user_name,
                    "task": todo["title"],
                    "completed": todo["completed"]})

    with open("todo_all_employees.json", "w") as jfile:
        json.dump(todo_all_employees, jfile)
