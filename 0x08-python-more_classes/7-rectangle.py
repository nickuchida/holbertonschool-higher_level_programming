#!/usr/bin/python3
'''
7-rectangle
'''


class Rectangle:
    '''
    class Rectangle
    '''
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        new = ''

        if (self.__width == 0) or (self.__height == 0):
            return ''
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    new += str(self.print_symbol)
                new += '\n'
            new = new[:-1]
            return new

    def __repr__(self):
        '''returns string representation'''
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        '''deletes instance of class'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
