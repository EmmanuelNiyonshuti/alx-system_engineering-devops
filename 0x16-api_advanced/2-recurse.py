#!/usr/bin/python3
"""
Make a GET request to Reddit API
"""
import requests

def append_to_hot_list(article_list, hot_list, index = 0):
    if index < len(article_list):
        hot_list.append(article_list[index]["data"]["title"])
        append_to_hot_list(article_list, hot_list, index + 1)

def recurse(subreddit, after=None, hot_list=None):
    """
    Recursive function to get titles of all hot articles for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    headers = {"User-Agent": "Learner/1.0 (Learner, python3-requests)"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?raw_json=1&after={after}"
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        obj = r.json()
        articles = obj["data"]["children"]

        append_to_hot_list(articles, hot_list)

        after = obj["data"]["after"]
        if after:
            return recurse(subreddit, after=after, hot_list=hot_list)
        else:
            return hot_list

    return None
