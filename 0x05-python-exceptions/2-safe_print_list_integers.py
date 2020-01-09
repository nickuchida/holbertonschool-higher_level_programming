#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element = 0
    for i in range(x):
        try:
            element += 1
            print('{:d}'.format(my_list[i]), end='')
        except(ValueError):
            continue
    print()
    return element
