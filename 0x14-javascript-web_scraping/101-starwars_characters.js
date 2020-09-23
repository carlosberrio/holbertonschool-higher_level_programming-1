#!/usr/bin/node

const request = require('request');
/* Request to every film character URL */
function charRequest (charURL) {
  return new Promise((resolve, reject) => {
    request(charURL, (error, response, body) => {
      if (error) reject(error);
      if (response.statusCode !== 200) {
        console.log('Invalid status code <' + response.statusCode + '>');
      }
      resolve(body);
    });
  });
}

/* Main Function - Request to Film URL */
function filmRequest () {
  const URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
  request(URL, async function (error, response, body) {
    for (const charURL of JSON.parse(body).characters) {
      if (!error) {
        const charJSON = await charRequest(charURL);
        console.log(JSON.parse(charJSON).name);
      } else {
        console.log('ERROR:');
        console.log(error);
      }
    }
  });
}

filmRequest(process.argv[2]);
