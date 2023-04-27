#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    _id = argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(base_url, _id)
    tasks_url = "{}todos?userId={}".format(base_url, _id)

    try:
        response = requests.get(user_url)
        response.raise_for_status()
        use_info = response.json()
        name = use_info["name"]

        res = requests.get(tasks_url)
        res.raise_for_status()
        tasks = res.json()

        done_tasks = 0
        total_tasks = 0
        completed_titles = []
        for task in tasks:
            if task["completed"]:
                done_tasks += 1
                completed_titles.append(task["title"])
            total_tasks += 1

        print("Employee {} ".format(name), end="")
        print("is done with tasks({}/{}):".format(done_tasks, total_tasks))
        for title in completed_titles:
            print("\t {}".format(title))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        exit(1)

