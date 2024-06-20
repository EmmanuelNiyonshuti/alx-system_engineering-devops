#!/usr/bin/python3

from dotenv import load_dotenv
import os
import requests

load_dotenv()

headers ={
    "DD-API-KEY": os.getenv("DD_API_KEY"),
    "DD-APPLICATION-KEY": os.getenv("DD_APPLICATION_KEY")
}
url = f"https://api.datadoghq.com/api/v1/dashboard"
r = requests.get(url, headers=headers)
if r.status_code == 200:
    data = r.json()
    dashboards = data["dashboards"]
    for k in dashboards:
        if k["id"]:
            with open("dashboard_id", "w") as f:
                f.write("{}\n".format(k["id"]))
            break
