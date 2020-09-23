#!/usr/bin/node

const request = require('request');
const URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(URL, function (err, response, body) {
  if (err) console.log(err);
  for (const charURL of JSON.parse(body).characters) {
    request(charURL, function (err, response, body) {
      if (!err) console.log(JSON.parse(body).name);
    });
  }
});
