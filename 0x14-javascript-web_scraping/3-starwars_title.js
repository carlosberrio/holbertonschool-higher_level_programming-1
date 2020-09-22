#!/usr/bin/node

const request = require('request');
const URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(URL, function (err, response, body) {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
