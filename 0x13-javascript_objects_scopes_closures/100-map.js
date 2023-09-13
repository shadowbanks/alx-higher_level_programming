#!/usr/bin/node
const data = require('./100-data.js');
if (data.list) {
  let temp = []; let i = 0;
  const arr = data.list;
  temp = arr.map((x) => x * i++);
  console.log(arr);
  console.log(temp);
}
