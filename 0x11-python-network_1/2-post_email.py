#!/usr/bin/python3
import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    # Values with urlencode --> email=hr%40holbertonschool.com
    data = data.encode('ascii')
    request = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
