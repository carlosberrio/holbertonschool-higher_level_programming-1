#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
request(URL, function (err, response, body) {
  if (err) console.log(err);
  const users = {};
  for (const todo of JSON.parse(body)) {
    if (todo.completed) users[todo.userId] = (users[todo.userId] || 0) + 1;
  }
  console.log(users);
});
