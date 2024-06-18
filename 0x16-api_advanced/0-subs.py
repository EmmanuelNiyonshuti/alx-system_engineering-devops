#!/usr/bin/python3
"""
Make a GET request to Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    headers = {"User-Agent": "Learner/1.0 (Learner, python3-requests)"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        obj = r.json()
        subs = obj["data"]["subscribers"]
        return subs
    if r.status_code == 404:
        return 0
