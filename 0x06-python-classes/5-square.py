#!/usr/bin/python3

'''5. Printing a square'''


class Square:
    """Definition of class, Square"""

    def __init__(self, size=0):
        """
        Initializes the class.

        Attr:
            size: Size of the sides of the square.
        """
        self.size = size

    @property
    def size(self):
        '''Get the size of the square'''
        return self.__size

    @size.setter
    def size(self, val=0):
        ''''Sets the value of size'''
        if type(val) is not int:
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        '''Calculate and return the area of the square'''
        return int(self.__size) ** 2

    def my_print(self):
        """Prints the square with character '#'"""
        print("\n".join('#' * self.__size for i in range(self.__size)]))
