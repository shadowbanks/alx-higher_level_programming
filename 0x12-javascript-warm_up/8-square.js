#!/usr/bin/node
const process = require('process');
const args = process.argv;
const num = Number(args[2]);
let i = 0;
let output = '';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (i++ < num) {
    output += 'X';
  }
  i = 0;
  while (i++ < num) {
    console.log(output);
  }
}
