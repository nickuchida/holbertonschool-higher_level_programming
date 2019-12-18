#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for i in my_string:
        if i != 'C' or i != 'c':
            new = new + i
    return new
