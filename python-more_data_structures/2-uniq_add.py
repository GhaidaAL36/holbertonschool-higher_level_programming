#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    for value in my_list:
        if value not in uniq:
            uniq.append(value)
    uniq_sum = 0
    for value in uniq:
        uniq_sum += value
    return (uniq_sum)
