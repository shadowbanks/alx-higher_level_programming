#!/usr/bin/node
const process = require('process');
const args = process.argv;
let num1 = Number(args[2]);
let num = 1;
if (isNaN(num1) || num1 <= 1) {
  num1 = 1;
}
function factorial (a) {
  if (a === 1) {
    return (1);
  }
  num = factorial(a - 1);
  return (num * a);
}

console.log(factorial(num1));
