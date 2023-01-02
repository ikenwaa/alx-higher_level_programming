#!/usr/bin/python3
"""1. Real definition of a rectangle"""


class Rectangle:
    """Rectangle class"""
    
    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle class.

        Args:
            width: represents the width of the rectangle.
            height: represents the height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value=0):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be an >= 0")
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
