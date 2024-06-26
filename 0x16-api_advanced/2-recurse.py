#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given
subreddit. If no results_from_response are found for the given
subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit."""

    subreddit_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(subreddit_url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results_from_response = response.json().get("data")
    after = results_from_response.get("after")
    count += results_from_response.get("dist")
    for child in results_from_response.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
