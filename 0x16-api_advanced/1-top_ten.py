#!/usr/bin/python3
"""
Make a GET request to Reddit API
"""
import requests

def top_ten(subreddit):
    """
    Make a GET request to /hot end point on Reddit API
    and prints the first 10 hot posts listed for a given subreddit.
    """
    headers = {"User-Agent": "Learner/1.0 (Learner, python3-requests)"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10&raw_json=1"
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        obj = r.json()
        for i in range(0, 9):
            titles = obj["data"]["children"][i]["data"]["title"]
            print(titles)
    else:
        print(None)
