#!/usr/bin/python3
"""funtion that queries the Reddit API"""
import requests
import sys


def number_of_subscribers(sub):
    """ Args:
        sub: subreddit name
        Return:
        number of subscibers or 0
    """

    headers = {'User-Agent': 'ComfortableYam96'}
    url = "https://www.reddit.com/r/{}/about.json".format(sub)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
