#!/usr/bin/python3

'''1. Square with size'''


class Square():
    """
    Square class with size attribute
    """

    def __init__(self, size=0):
        """
        Initialize class, Square.

        Args:
            size: The size of the side of the square.
        """
        self.__size = size
