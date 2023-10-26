#!/usr/bin/node
const request = require('request');
const args = process.argv;
const options = { json: true };

request(args[2], options, (error, response, body) => {
  if (error) return console.log(error);
  if (response.statusCode === 200) {
    const sub = '/people/13/';
    const str = JSON.stringify(body);
    const count = str.split(sub).length - 1;
    console.log(count);
    //console.log(str);
  }
});
