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
        """
        return the square area
        """
        return self.size * self.size
    
    def my_print(self):
        """
        prints square with the character #
        """
        if self.__size == 0:
            """checks if the size square is 0"""
            print()
            """prints an empty line"""
        else:
            for row in range(self.__size):
                print("#" * self.__size)
