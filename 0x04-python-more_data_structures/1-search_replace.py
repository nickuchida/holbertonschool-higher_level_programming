#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i, j in enumerate(my_list):
        if j == search:
            my_list[i] = replace
    return my_list
