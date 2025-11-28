#!/usr/bin/python3
def uppercase(str):
    result = ""

    for c in str:
        if 'a' <= c <= 'z':  # lowercase range
            result += chr(ord(c) - 32)  # convert to uppercase
        else:
            result += c

    print("{}".format(result))
