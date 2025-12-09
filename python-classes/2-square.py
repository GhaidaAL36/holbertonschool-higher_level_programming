#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """Represent a square with private optional attribute."""

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        :param size: The size of the square (must be an integer >= 0)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
