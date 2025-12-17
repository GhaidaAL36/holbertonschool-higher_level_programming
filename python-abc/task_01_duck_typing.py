#!/usr/bin/env python3
"""Module define abstract class named Shape 
with two abstract methods: area and perimeter
"""


from abc import ABC, abstractmethod

class Shape(ABC):
    """abstract class with two methods"""

    @abstractmethod
    def area(self):
        """return area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """return perimeter of shape"""
        pass

class Circle(Shape):
    """circle class that inherits from shape
    with initail radius
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """return area of circle"""
        return (3.14 * (self.radius ** 2))

    def perimeter(self):
        """return perimeter of circle"""
        return (2 * 3.14 * self.radius)

class Rectangle(Shape):
    """Rectangle class that inherits from shape
    with initail  width and height
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """return area of Rectangle """
        return self.width * self.height

    def perimeter(self):
        """return perimeter of Rectangle"""
        return 2 * self.height + 2 * self.width

def shape_info(shape):
        """function  that accepts an object of type Shape
        (by duck typing) 
        and prints its area and perimeter
        """
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}") 