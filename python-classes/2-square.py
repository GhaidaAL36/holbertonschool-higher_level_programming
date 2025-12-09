#!/usr/bin/python3
"""defines a square by Private instance attribute: size"""


class Square:
    """Represent a square with private optional attribute """
    def __init__(self, size=0):
        if isinstance(size, int): 
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
