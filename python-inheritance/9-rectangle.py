#!/usr/bin/python3
"""
Module that defines a Rectangle class, inheriting from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height (validated)."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
    
    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
