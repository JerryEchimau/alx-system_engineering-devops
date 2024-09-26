#!/usr/bin/python3
"""
Module to recursively fetch and return titles of all hot posts from a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to retrieve titles of all hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the titles. Defaults to [].
        after (str, optional): Used for pagination, indicating the next page. Defaults to None.

    Returns:
        list: List of titles of hot posts, or None if invalid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if data['after']:
            return recurse(subreddit, hot_list, data['after'])
        else:
            return hot_list
    else:
        return None

