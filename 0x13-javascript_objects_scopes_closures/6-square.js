#!/usr/bin/node
const Squares = require('./5-square.js');

class Square extends Squares {
  charPrint (c) {
    let printChar = 'X';
    if (c) {
      printChar = c;
    }
    let temp = ''; let i = 0;
    while (i++ < this.width) {
      temp += printChar;
    }
    i = 0;
    while (i++ < this.height) {
      console.log(temp);
    }
  }
}

module.exports = Square;
