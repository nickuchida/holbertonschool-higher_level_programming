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

    def update(self, *args, **kwargs):
        '''updates class square'''
        argnum = len(args)
        if argnum >= 1:
            self.id = args[0]
        if argnum >= 2:
            self.size = args[1]
        if argnum >= 3:
            self.x = args[2]
        if argnum >= 4:
            self.y = args[3]
        if argnum == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
