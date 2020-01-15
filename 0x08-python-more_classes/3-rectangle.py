#!/usr/bin/python3
'''
0-rectangle
'''


class Rectangle:
    '''
    class Rectangle
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        'getter'
        return self.__width
    @width.setter
    def width(self, value):
        'setter'
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''getter'''
        return self.__height
    @height.setter
    def height(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''returns the rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns the rectangle perimeter'''
        return (self.__width + self.__height) * 2

    def __str__(self):
        '''print rectangle'''
        str = ''

        if (self.__width == 0) or (self.__height == 0):
            return ''
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    str += '#'
                str += '\n'
            str = str[:-1]
            return str

Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
