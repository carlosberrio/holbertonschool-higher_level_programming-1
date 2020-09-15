#!/usr/bin/node
isNaN(Number(process.argv[2]))
  ? console.log('Not a number')
  : console.log(`My number: ${process.argv[2]}`);
