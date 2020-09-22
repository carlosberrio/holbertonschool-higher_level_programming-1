#!/usr/bin/node

const list = [];
exports.logMe = function (item) {
  list.push(item);
  console.log(`${list.indexOf(item)}: ${list[list.indexOf(item)]}`);
};
