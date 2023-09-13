#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0; let count = 0;
  if (list) {
    while (i < list.length) {
      if (searchElement === list[i++]) {
        count++;
      }
    }
  }
  return (count);
};
