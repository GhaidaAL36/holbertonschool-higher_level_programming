#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_element = []
    for value in set_1:
        if value not in set_2:
            diff_element.append(value)
    for value in set_2:
        if value not in set_1:
            diff_element.append(value)
    return (diff_element)
