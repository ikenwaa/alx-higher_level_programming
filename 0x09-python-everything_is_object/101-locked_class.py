#!/usr/bin/python3
"""This defines a locked class."""


class LockedClass():
    """
    This class prevents dynamic creation
    of instance attributes except if the
    instance is called `first_name`
    """
    __slots__ = "first_name"
