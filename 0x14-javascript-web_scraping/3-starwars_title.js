#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
const options = { json: true };

request(url, options, (error, response, body) => {
  if (error) return console.log(error);
  if (response.statusCode === 200) {
    console.log(body.title);
  }
});
