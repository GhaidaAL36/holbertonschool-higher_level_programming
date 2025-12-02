#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for value in set_1:
        if value in set_2:
            common.append(value)
    return (common)
