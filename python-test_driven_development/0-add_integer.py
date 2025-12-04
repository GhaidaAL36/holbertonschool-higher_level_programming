#!/usr/bin/python3
"""
This module contains a function that adds two integers.
It checks types and casts floats to integers before adding.
The function returns the sum as an integer.
"""

def add_integer(a, b=98):
    """
    Adds two integers a and b after validation.

    Floats are casted to integers. Raises TypeError if invalid.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
