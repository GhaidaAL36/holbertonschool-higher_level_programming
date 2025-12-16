#!/usr/bin/python3
"""
Module that defines a function to list all attributes
and methods of an object.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
