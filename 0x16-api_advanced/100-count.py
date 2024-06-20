#!/usr/bin/python3
"""
This script fetches hot articles from a given subreddit
and counts the occurrences of specific keywords in the titles.
"""

from collections import defaultdict
import requests


def append_titles(articles, titles, index=0):
    """
    append all titles to the titles list.
    """

    if index < len(articles):
        titles.append(articles[index]["data"]["title"])
        append_titles(articles, titles, index + 1)


def count_keywords(titles, word_list):
    """
    count the key words in the titles.
    """

    keyword_count = defaultdict(int)
    for title in titles:
        words = title.lower().split()
        for word in word_list:
            keyword_count[word.lower()] += words.count(word.lower())
    return keyword_count


def print_sorted_results(keyword_count):
    """
    Prints the keyword counts sorted by count (descending)
    and then alphabetically.
    """
    sorted_kw = sorted(keyword_count.items(), key=lambda i: (-i[1], i[0]))
    for w, c in sorted_kw:
        if c > 0:
            print("{}: {}".format(w, c))


def count_words(subreddit, word_list, after=None, titles=None):
    """
    Recursively Querries the Reddit API,
    parses titles of all hot articles,
    and print a sorted count of given key words.
    """

    if titles is None:
        titles = []

    url = "https://www.reddit.com/r/{}/hot.json?after={}&raw_json=1".format(
        subreddit, after)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        obj = r.json()
        data = obj["data"]["children"]
        append_titles(data, titles)

        after = obj["data"]["after"]
        if after:
            count_words(subreddit, word_list, after=after, titles=titles)
        else:
            keyword_count = count_keywords(titles, word_list)
            print_sorted_results(keyword_count)
            return keyword_count
    return 0
