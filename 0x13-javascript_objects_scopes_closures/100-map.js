#!/usr/bin/node
const data = require('./100-data.js');
if (data.list) {
  let temp = [];
  const arr = data.list;
  temp = arr.map((x) => x * arr.indexOf(x));
  console.log(arr);
  console.log(temp);
}
