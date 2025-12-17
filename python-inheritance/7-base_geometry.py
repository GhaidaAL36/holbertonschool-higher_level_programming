#!/usr/bin/python3
"""This class is an empty class which is named BaseGeometry"""


class BaseGeometry:
    """A kinda empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
