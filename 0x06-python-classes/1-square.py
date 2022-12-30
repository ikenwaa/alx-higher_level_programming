#!/usr/bin/python3

'''1. Squatre with size'''

class Square():
    """
    Square class with size attribute
    """

    def __init__(self, size=0):
        """
        Initilaize class, Square.

        Args:
            size (int): The size os the side of the square.
        """
        self.__size = size
