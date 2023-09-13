#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
