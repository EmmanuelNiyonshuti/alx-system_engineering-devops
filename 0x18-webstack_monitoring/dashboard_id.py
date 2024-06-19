#!/usr/bin/python3

import requests


headers ={
    "DD-API-KEY": "32195ca47053fd4c494de0390da37fee",
    "DD-APPLICATION-KEY": "5eb2afed74682b09d9668be89d7ecf3e30b48d3e"
}
url = f"https://api.datadoghq.com/api/v1/dashboard"
r = requests.get(url, headers=headers)
if r.status_code == 200:
    data = r.json()
    dashboards = data["dashboards"]
    for k in dashboards:
        print(k["id"])

