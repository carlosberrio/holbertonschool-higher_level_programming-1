#!/usr/bin/python3
"""
Module that takes in a URL, sends a request to the URL and displays the body
of the response.  If the HTTP status code is greater than or equal to 400,
print: Error code: <Status Code>.
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
