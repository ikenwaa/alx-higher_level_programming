#!/usr/bin/python3
'''9. A square is a rectangle'''


class Rectangle:
    '''Rectangle class'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        Intializes the Rectangle class.

        Args:
            width: Represents the width of the rectangle
            height: Represents the height of the triangle
        '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        
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
        rect = "\n".join([str(self.print_symbol) * self.__width
                        for row in range(self.__height)])
        return rect

    def __repr__(self):
        '''String representation to create new instance'''
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        '''Deletes instance of Rectangle class'''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Compares and returns biggest rectangle'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle") 
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        '''Return Rectangle instance with width == height == size'''
        return cls(size, size)