#!/usr/bin/python3
"""
queries the Reddit API
parses the title of all hot articles
prints a sorted count of given keywords(case-insensitive, delimited by spaces)
"""

from collections import Counter
import requests


def count_words(subreddit, word_list):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My User Agent"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            
            titles = [post["data"]["title"] for post in posts]
            word_count = Counter()
            
            for title in titles:
                words = title.lower().split()
                filtered_words = [word for word in words
                                  if word.rstrip('.!_') not in word_list]
                word_count.update(filtered_words)
            
            if word_count:
                sorted_count = sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0]))
                
                for word, count in sorted_count:
                    print("{}: {}".format(word, count))
            else:
                pass
        else:
            pass
    except requests.exceptions.RequestException:
        pass
