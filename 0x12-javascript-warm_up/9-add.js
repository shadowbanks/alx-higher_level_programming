#!/usr/bin/node
const process = require('process');
const args = process.argv;
const num1 = Number(args[2]);
const num2 = Number(args[3]);

function add(a, b){
	console.log(a + b);
}

add(num1, num2);
