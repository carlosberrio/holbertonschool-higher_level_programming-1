#!/usr/bin/node

const request = require('request');
const base64 = require('base-64');
const utf8 = require('utf8');

const CONSUMER_KEY = process.argv[2];
const CONSUMER_SECRET = process.argv[3];
const SEARCH = process.argv[4];
const SINGLEKEY = base64.encode(utf8.encode(CONSUMER_KEY + ':' + CONSUMER_SECRET));
let bearerToken = '';

request.post({
  url: 'https://api.twitter.com/oauth2/token',
  headers: {
    Authorization: 'Basic ' + SINGLEKEY,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },
  form: { grant_type: 'client_credentials' }
}, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.log(`Error: <${response.statusCode}>\n`, error);
  }
  bearerToken = JSON.parse(body).access_token;
  /* Request to get recent tweets */
  request.get({
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    headers: { Authorization: 'Bearer ' + bearerToken },
    qs: {
      q: SEARCH,
      result_type: 'recent',
      count: 5
    }
  }, function (error, response, body) {
    if (error || response.statusCode !== 200) {
      console.log(`Error: <${response.statusCode}>\n`, error);
    }
    for (const tweet of JSON.parse(body).statuses) {
      console.log(`[${tweet.id}] ${tweet.text} by ${tweet.user.name}`);
    }
  });
});
