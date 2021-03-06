#!/usr/bin/python3
"""
 func that gathers data from an API and exports it to JSON file
Records all tasks from all employees
"""


if __name__ == "__main__":
    import requests
    import sys
    import json

    users_req = requests.get("https://jsonplaceholder.typicode.com/users/")
    tasks_req = requests.get("https://jsonplaceholder.typicode.com/todos")
    json_data = {}
    value_list = []
    for user in users_req.json():
        for each in tasks_req.json():
            if user["id"] == each["userId"]:
                each.update([("username", user["username"])])
                each.pop("id")
                each.pop("userId")
                each.update([("task", each["title"])])
                each.pop("title")
                value_list.append(each)
        json_data[user["id"]] = value_list
        value_list = []

    with open("todo_all_employees.json", 'w', encoding='utf=8') as file:
        json.dump(json_data, file, indent=4)
