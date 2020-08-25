#!/usr/bin/python3
"""
Module that:
Displays five results: [<Tweet ID>] <Tweet text> by <Tweet owner name>
* First argument must be the Consumer Key (API Key)
* Second argument must be the Consumer Secret (API Secret)
* Third argument must be the search string
"""
import base64
import requests
from sys import argv, exit

if __name__ == '__main__':
    CONSUMER_KEY = argv[1]
    CONSUMER_SECRET = argv[2]
    # Twitter API requires a single key that is a string of a base64 encoded
    # version of the two keys separated by a colon: /base64.encode()/
    single_key = '{}:{}'.format(CONSUMER_KEY, CONSUMER_SECRET).encode('ascii')
    b64_encoded_key = base64.b64encode(single_key)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    # post request to the authentication endpoint to obtain a Bearer Token:
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    if auth_resp.status_code != 200:
        raise Exception(
            "Authentication request returned an error: [{}] - {}".format(
                auth_resp.status_code, auth_resp.reason
            )
        )
    access_token = auth_resp.json().get('access_token')  # -> Bearer Token
    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    search_params = {
        'q': argv[3],
        'result_type': 'recent'
    }
    # -- Content request according search string --:
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    response = requests.get(search_url, headers=search_headers,
                            params=search_params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.reason
            )
        )
    # -- Response content to JSON --:
    tweet_data = response.json()
    for count, tweet in enumerate(tweet_data['statuses']):
        if count == 5:
            break
        id, text = tweet.get('id'), tweet.get('text')
        name = tweet.get('user').get('name')
        print("[{}] {} by {}".format(id, text, name))
