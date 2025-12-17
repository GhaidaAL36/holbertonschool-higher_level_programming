#!/usr/bin/python3
"""Module with empty class BaseGeometry"""


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """method raise an Exception with a message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
