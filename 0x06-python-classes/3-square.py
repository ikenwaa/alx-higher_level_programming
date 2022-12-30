#!/usr/bin/python3

'''3. Area of a square'''


class Square():
    '''Definition of class, Square'''

    def __init__(self, size=0):
        '''
        Initialization of Square

        Attr:
            size: Size of the sides of the square
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calcuates the area of a square
        """
        return int(self.__size) * int(self.__size)
