#!/usr/bin/python3
"""
Module that fetches https://intranet.hbtn.io/status with the package requests
and displays: type of response content and content.
"""
import requests

if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:"
          "\n\t- type: {}"
          "\n\t- content: {}".format(type(response.text), response.text))
