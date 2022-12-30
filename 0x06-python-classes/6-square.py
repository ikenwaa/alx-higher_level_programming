#!/usr/bin/python3

'''6. Coordinates of a square'''


class Square:
    """Definition of class, Square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the class.

        Attr:
            size: Size of the sides of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''Get the position'''
        return self.__position

    @position.setter
    def position(self, val):
        '''Sets position to tuple if val if of 2 +ve ints'''
        if type(val) is not tuple or len(val) != 2 or \
            type(val[0]) is not int or type(val[1]) is not int or \
                val[0] < 0 or val[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = val

    def area(self):
        '''Calculate and return the area of the square'''
        return int(self.__size) ** 2

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
