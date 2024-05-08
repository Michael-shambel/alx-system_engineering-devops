#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code == 200:
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
