#!/usr/bin/python3


def print_square(size):
    """Prints a square of #s"""
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    if size == 0:
        print('')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
