#!/usr/bin/python3
"""
Module that takes in a letter and sends a POST request to an url
with the letter as a parameter. Prints JSON -> [<id>] <name>
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    value = "" if len(argv) == 1 else argv[1]
    response = requests.post(url, data={'q': value})
    if response.headers.get('content-type') == 'application/json':
        json = response.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
