#!/usr/bin/python3
"""
Module that defines a function to check whether an object is an instance of,
or an instance of a class that inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of a_class or
    an instance of a class that inherited from a_class.
    Otherwise, return False.
    """
    return isinstance(obj, a_class)
