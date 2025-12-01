#!/usr/bin/python3
def max_integer(my_list=[]):
    maximu = 0
    if not my_list:
        return (None)
    for x in my_list:
        if x > maximu:
            maximu = x
    return (maximu)
