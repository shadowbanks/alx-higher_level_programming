#!/usr/bin/node
const process = require('process');
const args = process.argv;
const numOfArg = args.length;
let max; let num;
if (numOfArg < 4) {
  max = 0;
} else {
  num = args.slice(2).map(str => Number(str));
  num.sort((a, b) => b - a);
  max = num[1];
}

console.log(max);
