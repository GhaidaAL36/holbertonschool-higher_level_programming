#!/usr/bin/node

const numbers_list = process.argv.slice(2).map(Number);
const max_num = Math.max(...numbers_list);
let second_max = Math.min(...numbers_list);

if (numbers_list.length === 0 || numbers_list.length === 1) {
    console.log(0)
} else {
    for (let i = 0; i < numbers_list.length; i++) {
        if (second_max < numbers_list[i] && numbers_list[i] < max_num) {
            second_max = numbers_list[i];
        }
    } console.log(second_max);
}
