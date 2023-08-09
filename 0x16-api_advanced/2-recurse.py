#!/usr/bin/python3
"""
Task 1, but using a recursive function
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My User Agent"}

    params = {"after": after} if after else {}

    try:
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]

            for post in posts:
                title = post["data"]["title"]
                hot_list.append(title)

            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list=hot_list, after=after)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
