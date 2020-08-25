#!/usr/bin/python3
"""
Module that:
The first argument must be the Consumer Key (API Key)
The second argument must be the Consumer Secret (API Secret)
The third argument must be the search string
Display only 5 results: [<Tweet ID>] <Tweet text> by <Tweet owner name>
"""
import base64
import requests
from sys import argv, exit

if __name__ == '__main__':
    # Consumer Key (API Key)
    CONSUMER_KEY = argv[1]
    # Consumer Secret (API Secret)
    CONSUMER_SECRET = argv[2]
    # twitter API requires a single key that is a string of a
    # base64 encoded version of the two keys separated by a colon:
    # base64.encode()
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

    if auth_resp.status_code >= 400:
        print("Error code: {} - {}".format(auth_resp.status_code,
                                           auth_resp.reason))
        exit()

    token_type = auth_resp.json().get('token_type')
    access_token = auth_resp.json().get('access_token')

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    search_params = {
        'q': argv[3],
        'result_type': 'recent'
    }
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    response = requests.get(search_url, headers=search_headers,
                            params=search_params)

    if response.status_code >= 400:
        print("Error code: {} - {}".format(response.status_code,
                                           response.reason))
        exit()

    tweet_data = response.json()
    for count, tweet in enumerate(tweet_data['statuses']):
        if count == 5:
            break
        id, text = tweet.get('id'), tweet.get('text')
        name = tweet.get('user').get('name')
        print("[{}] {} by {}".format(id, text, name))
