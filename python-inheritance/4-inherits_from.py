#!/usr/bin/python3
"""
Module that defines a function to check whether an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    from a_class, directly or indirectly, but not an instance of
    a_class itself. Otherwise, return False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
