#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print('0{:d}'.format(i), end=', ')
    elif i > 10 and i < 99:
        print(i, end=', ')
    else:
        print(i)
