#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns
the number of subscripbers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0"""


def number_of_subscribers(subreddit):
    """query number of subscribers in a given subreddit"""

    import requests

    subreddit_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(subreddit_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
