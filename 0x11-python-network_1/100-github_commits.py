#!/usr/bin/python3
"""
Module that prints all commits by: `<sha>: <author name>` (one by line)
* The first argument will be the repository name
* The second argument will be the owner name
API INFO -> GET /repos/:owner/:repo/commits
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    response = requests.get(url)
    json = response.json()
    for n in range(10):
        # 3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
        sha = json[n]['sha']
        name_request = requests.get(json[n]['author']['url'])
        author = name_request.json().get('name')
        print("{}: {}".format(sha, author))
