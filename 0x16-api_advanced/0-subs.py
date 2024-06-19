#!/usr/bin/python3
"""
Contains a function that makes a GET request to the Reddit API
to get the number of subscribers for a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers. Returns 0 if the subreddit is invalid
    or in case of an error.
    """
    headers = {"User-Agent": "Learner/1.0 (Learner, python3-requests)"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json?raw_json=1"
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        try:
            obj = r.json()
            subs = obj["data"]["subscribers"]
            return subs
        except (KeyError, TypeError):
            return 0
    return 0
