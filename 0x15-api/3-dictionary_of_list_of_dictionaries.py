#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
from unicodedata import name
import requests
from sys import argv

if __name__ == "__main__":

    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users".format(api_url)).json()
    todos = requests.get("{}todos".format(api_url)).json()

    with open("todo_all_employees.json", "w") as file:
        my_dict = {}

        for x in todos:
            if x["userId"] not in my_dict:
                my_dict[x["userId"]] = []
            id_user = next(d for d in user if d['id'] == x["userId"])
            my_dict[x["userId"]].append({"username": id_user["username"],
                                         "task": x["title"],
                                         "completed": x["completed"]})
        json.dump(my_dict, file)
