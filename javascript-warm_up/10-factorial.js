#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);

function factorial (n) {
  if (Number.isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(arg));
