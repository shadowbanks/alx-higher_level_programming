#!/usr/bin/node
const process = require('process');
const args = process.argv;
let num = Number(args[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (num--) {
    console.log('C is fun');
  }
}
