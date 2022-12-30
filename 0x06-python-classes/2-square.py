#!/usr/bin/python3

"""2. Size validation"""


class Square(self):
    """
    Definition of class, Square.
    """

    def __init__(self, size=0):
        """
        Initialize class, Square

        Attr:
            size: Size of the sides of the square.
        """

        if type(size) is not int:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size
