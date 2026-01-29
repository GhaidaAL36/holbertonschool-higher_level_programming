#!/usr/bin/node

const numbersList = process.argv.slice(2).map(Number);
const maxNum = Math.max(...numbersList);
let secondMax = Math.min(...numbersList);

if (numbersList.length === 0 || numbersList.length === 1) {
  console.log(0);
} else {
  for (let i = 0; i < numbersList.length; i++) {
    if (secondMax < numbersList[i] && numbersList[i] < maxNum) {
      secondMax = numbersList[i];
    }
  }
  console.log(secondMax);
}
