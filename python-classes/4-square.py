#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """This class defines a square with a specififc size"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size
        """returns the size of the square"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        """TypeError: if size is not an integer"""
        if value < 0:
            raise ValueError("size must be >= 0")
        """ValueError: if size is less than 0"""
        self.__size = value
        """Returns the value"""

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2
        """returns the area of the square"""