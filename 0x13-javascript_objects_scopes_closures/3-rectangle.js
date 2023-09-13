#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print(){
    let temp = "", i = 0;
    while (i++ < this.width){
      temp += "X";
    }
    i = 0;
    while (i++ < this.height){
      console.log(temp);
    }
  }
}

module.exports = Rectangle;
