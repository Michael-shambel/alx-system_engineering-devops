#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""
import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {}

    if not word_list:
        return
    
    if after:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

        after = data['data'].get('after')
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
