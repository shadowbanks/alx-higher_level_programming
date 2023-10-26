#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const options = { json: true };
const result = {};

request(url, options, (err, res, body) => {
  if (err) return console.log(err);

  if (res.statusCode === 200) {
    for (const task of body) {
      if (task.completed) {
        if (result[task.userId]) { result[task.userId] += 1; } else { result[task.userId] = 1; }
      }
    }
    console.log(result);
  }
});
