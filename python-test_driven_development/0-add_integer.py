#!/usr/bin/python3
"""
This module provides a function to add two integers together.
The function ensures that both inputs are integers or floats before performing the addition.
If a float is provided, it will be cast to an integer.
If an invalid type is provided, the function raises a TypeError with a clear message.
This module does not import any external modules and demonstrates simple type checking in Python.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats after type validation.
    Floats are cast to integers before addition.
    Raises TypeError if inputs are invalid.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
