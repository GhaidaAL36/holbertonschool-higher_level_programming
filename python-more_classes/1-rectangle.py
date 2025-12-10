#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return self.__width
    """returns the width of the rectangle"""
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        """TypeError: if width is not an integer"""
        if value < 0:
            raise ValueError("width must be >= 0")
        """ValueError: if width is less than 0"""
        self.__width = value
        """set the width"""
    
    @property
    def height(self):
        return self.__height
        """returns the height of the rectangle"""
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """TypeError: if height is not an integer"""
        if value < 0:
            raise ValueError("height must be >= 0")
        """ValueError: if height is less than 0"""
        self.__height = value
        """set the height"""