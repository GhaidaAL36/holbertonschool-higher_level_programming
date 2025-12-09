#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """Represent a square with private optional attribute."""
    def __init__(self, size=0):
        self.size = size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
 
    def area(self):
        """
        return the square area
        """
        return self.size * self.size