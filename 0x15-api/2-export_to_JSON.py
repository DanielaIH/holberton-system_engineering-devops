#!/usr/bin/python3
"""Python script to export data in the JSON format."""

import json
import requests
from sys import argv

if __name__ == "__main__":
    tasks = []

    id_e = int(argv[1])
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(api_url, id_e)).json()
    todos = requests.get("{}users/{}/todos".format(api_url, id_e)).json()

    filepath = "{}.json".format(id_e)
    with open(filepath, "w") as file:
        my_dict = {}
        my_dict[id_e] = []
        for x in todos:
            my_dict[id_e].append({"task": x["title"],
                                  "completed": x["completed"],
                                  "username": user["username"]})
        print(my_dict)
        json.dump(my_dict, file)
