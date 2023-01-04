#!/usr/bin/python3
"""Def locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new attributes
    except attribut called 'first_name'.
    """

    __slots__ = ["first_name"]
