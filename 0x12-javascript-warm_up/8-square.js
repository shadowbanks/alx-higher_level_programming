#!/usr/bin/node
const process = require('process');
const args = process.argv;
const num = Number(args[2]);
let i = 0;
let output = '';
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (i++ < num && num > 0) {
    output += 'X';
  }
  i = 0;
  while (i++ < num) {
    console.log(output);
  }
}
