#!/usr/bin/python3
"""Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""

import requests
import sys


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""

    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(subreddit_url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            data_children = response.json().get('data').get('children')
            for i in range(10):
                print(data_children[i].get('data').get('title'))
        else:
            print("None")
    except Exception as e:
        print("None")
