#!/usr/bin/python3
import urllib.request
import urllib.error
from sys import argv

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
