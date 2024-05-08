#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """return number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code == 200:
        subscribers = data['data']['subscribers'] 
        return subscribers
    else:
        return 0   
