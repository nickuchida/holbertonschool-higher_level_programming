#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    for i in range(x):
        try:
            ++element
            print(my_list[i], end='')
        except:
            break
    print()
    return element
