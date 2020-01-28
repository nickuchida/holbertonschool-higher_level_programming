#!/usr/bin/python3
'''
module square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    square inherits from rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''initializes variables'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str'''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        '''getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter'''
        self.width = value
        self.height = value

    def to_dictionary(self):
        '''returns dictionary representation'''
        dicrep = {}
        dicrep['id'] = self.id
        dicrep['size'] = self.size
        dicrep['x'] = self.x
        dicrep['y'] = self.y
        return dicrep
