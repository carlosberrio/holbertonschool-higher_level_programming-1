#!/usr/bin/node
process.argv.length === 2 ? console.log('No argument')
  : process.argv.length === 3 ? console.log('Argument found')
    : console.log('Arguments found');
