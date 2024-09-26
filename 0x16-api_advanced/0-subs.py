#!/usr/bin/python3
"""
This module defines a function to retrieve the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a subreddit from the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers to the subreddit, or 0 if not found.
    """
    url = f"https://www.reddit.com/r/nairobi/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)'
                    ' Gecko/20100101 Firefox/15.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except KeyError:
            return 0
    else:
        return 0
