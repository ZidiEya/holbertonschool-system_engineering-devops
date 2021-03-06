#!/usr/bin/python3
"""
func to queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
for a given subreddit. if an invalid subreddit is given,
the func must return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of total the subscribers"""
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)
    response = response.json()
    if 'data' in response:
        return (response.get('data').get('subscribers'))

    else:
        return (0)
