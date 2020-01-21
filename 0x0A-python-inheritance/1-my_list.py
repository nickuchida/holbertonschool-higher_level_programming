#!/usr/bin/python3
'''
1
'''


class MyList(list):
    '''a class that inherits from list'''
    def print_sorted(self):
        '''prints sorted list'''
        print(sorted(self))
