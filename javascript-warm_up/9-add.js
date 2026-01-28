#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  a = Number(arg1);
  b = Number(arg2);

  if (a && b) {
    return (a + b);
  } else {
    return (NaN);
  }
}

console.log(add(arg1, arg2));
