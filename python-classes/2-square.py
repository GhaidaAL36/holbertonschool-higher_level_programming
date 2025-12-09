#!/usr/bin/python3
"""defines a square with size validation"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a square.
        Args:
            size (int): size of the square (default 0)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is < 0
        """
        if isinstance(size, int): 
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
