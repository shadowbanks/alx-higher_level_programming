#!/usr/bin/node
const process = require('process');
const arg = process.argv;
const num = Number(arg[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(num);
}
