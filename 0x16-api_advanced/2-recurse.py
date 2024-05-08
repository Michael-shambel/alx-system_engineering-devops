#!/usr/bin/python3
"""
 recursive function that queries the Reddit API and returns a list containing
 the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ecursive function that queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code == 200:
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
