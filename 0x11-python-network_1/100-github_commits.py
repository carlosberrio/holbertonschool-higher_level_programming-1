#!/usr/bin/python3
"""
Module that prints all commits by: `<sha>: <author name>` (one by line)
* The first argument will be the repository name
* The second argument will be the owner name
API INFO -> GET /repos/:owner/:repo/commits
"""
import requests
from sys import argv, exit

if __name__ == '__main__':
    owner = argv[2]
    rep = argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, rep)
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {} - {}".format(response.status_code,
                                           response.reason))
        exit()
    try:
        json = response.json()
        if json:
            for count, item in enumerate(json):
                if count < 10:
                    sha = item.get('sha')
                    name = item.get('commit').get('author').get('name')
                    print("{}: {}".format(sha, name))
                else:
                    break
        else:
            print("No result: Empty file")
    except ValueError:
        print("Not a valid JSON")
