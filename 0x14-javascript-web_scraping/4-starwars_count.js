#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
request(URL, function (err, response, body) {
  if (err) console.log(err);
  let count = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      count += (character.includes('/18/')) ? 1 : 0;
    }
  }
  console.log(count);
});
