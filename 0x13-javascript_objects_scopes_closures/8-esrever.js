#!/usr/bin/node
exports.esrever = function (list) {
  const temp = []; let i = 0;
  if (list) {
    i = list.length - 1;
  }
  while (i >= 0) {
    temp.push(list[i--]);
  }
  return (temp);
};
