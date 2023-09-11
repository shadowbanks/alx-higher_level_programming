#!/usr/bin/node
const process = require('process');
const args = process.argv;
const numOfArgs = args.length;
if (numOfArgs === 2) {
  console.log('No argument');
} else if (numOfArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
