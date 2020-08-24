#!/usr/bin/python3
"""
Module takes an Github credentials (username and password)
and uses the Github API to display the user id
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    headers = {'Authorization': 'token ' + argv[2]}
    response = requests.get(url, headers=headers)
    print(response.json().get('id'))
