#!/usr/bin/node
const data = require('./101-data.js');
if (data.dict) {
  // Create an empty dictionary to hold the result
  const temp = {};
  // datas to hold the dictionary in the object (occurrences by user id)
  const datas = data.dict;

  // loop through the keys of the {datas} "user id"
  for (const x in datas) {
    // elem holds the value of dictionary fro each key "number of occurrences"
    const elem = datas[x];
    // Check if the number of occureneces is already a key
    if (elem in temp) {
      // append "user id" if number of occurrence already exist
      temp[elem].push(x);
    } else {
    // create a new number of occurence with "user id" as value
      temp[elem] = [x];
    }
  }
  console.log(temp);
}
