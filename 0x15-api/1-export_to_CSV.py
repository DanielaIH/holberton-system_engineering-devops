#!/usr/bin/python3
"""Python script to export data in the CSV format."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    tasks = []

    id_e = int(argv[1])
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(api_url, id_e)).json()
    todos = requests.get("{}users/{}/todos".format(api_url, id_e)).json()

    filepath = "{}.csv".format(id_e)
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)

        for x in todos:
            writer.writerow([id_e, user["username"], x["completed"],
                            x["title"]])
    file.close()
