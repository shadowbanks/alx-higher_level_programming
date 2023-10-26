#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (error) return console.log(error);
  if (response.statusCode === 200) {
    fs.writeFile(args[3], body, 'utf8', err => {
      if (err) return console.log(err);
    });
  }
});
