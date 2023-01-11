#!/usr/bin/python3
"""Defines a class to inherit list."""


class MyList(list):
    """Implements print_sort."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
