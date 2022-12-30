#!/usr/bin/python3

"""4. Access and update private attribute"""


class Square:
    """Definition of class, Square."""

    def __init__(self, size=0):
        """
        Initializes Square

        Attr:
            size: Size of the sides of a square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value=0):
        '''Set the value of size'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Calculate and return the area of the square'''
        return int(self.__size) ** 2
