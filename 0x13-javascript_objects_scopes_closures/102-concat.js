#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const arg = process.argv;

function concatFile (args) {
  fs.readFile(args[2], 'utf-8', (err, fileA) => {
    if (err) {
      console.log(err);
      return;
    }
    fs.readFile(args[3], 'utf-8', (err, fileB) => {
      if (err) {
        console.log(err);
        return;
      }
      const fileC = fileA + fileB;
      fs.writeFile(args[4], fileC, 'utf-8', (err) => {
        if (err) {
          console.log(err);
        }
      });
    });
  });
}
concatFile(arg);
