#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""

class MyList(list):
    """MyList class that extends list with a sorted print method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
