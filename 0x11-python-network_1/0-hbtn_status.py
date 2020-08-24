#!/usr/bin/python3
"""
Module that fetches https://intranet.hbtn.io/status and prints content response
"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        res = resp.read()
        print("Body response:"
              "\n\t- type: {}"
              "\n\t- content: {}"
              "\n\t- utf8 content: {}"
              .format(type(res), res, res.decode('utf-8')))
