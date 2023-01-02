#!/usr/bin/python3
'''2. Area and Perimeter'''


class Rectangle:
    '''Rectangle class'''
    def __init__(self, width=0, height=0):
        '''
        Intializes the Rectangle class.

        Args:
            width: Represents the width of the rectangle
            height: Represents the height of the triangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Get the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value=0):
        '''Set the width of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Get the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value=0):
        '''Set the height of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Calculate the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculate the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''Prints the rectangle with #'s'''
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = "\n".join(['#' * self.__width for row in range(self.__height)])
        return rect

    def __repr__(self):
        '''String representation to create new instance'''
        return "Rectangle({:d}, {:d})".format(self.width, self.height)