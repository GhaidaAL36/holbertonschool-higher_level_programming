#!/usr/bin/node

const x = process.argv[2];

if (Number(x)) {
  const num = Number(x);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
