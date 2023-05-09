#!/usr/bin/python3
"""
100-count module
"""
import requests
import time


def count_words(subreddit, word_list, titles={}, after="", count=0):
    """
         a recursive function that queries the Reddit API,
         parses the title of all hot articles, and prints
         a sorted count of given keywords
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        for word in c.get("data").get("title").split():
            if word in word_list:
                word = word.lower()

                if word not in titles:
                    titles[word] = 0

                titles[word] += 1

    if after is not None:
        return count_words(subreddit, word_list, titles, after, count)

    titles = sorted(titles.items(), key=lambda y: y[1], reverse=True)
    list = []

    for i in range(len(titles)):
        j = i + 1

        while j < len(titles) and titles[i][1] == titles[j][1]:
            list.append(titles[i])
            i += 1
            j += 1

        if list != []:
            list.append(titles[i])
            list = sorted(list, key=lambda y: y[0])

            for x in range(len(list)):
                print(list[x][0] + ":", list[x][1])

            list = []

        print(titles[i][0] + ":", titles[i][1])
