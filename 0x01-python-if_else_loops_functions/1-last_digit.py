#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0 or number == 0:
    lastdigit = number % 10
else:
    lastdigit = - ((- number) % 10)

print('Last digit of {:d}'.format(number), end =' ')
if lastdigit > 5:
    print('is {:d} and is greater than 5'.format(lastdigit))
elif lastdigit == 0:
    print('is {:d} and is 0'.format(lastdigit))
else:
    print('is {:d} and is less than 6 and not 0'.format(lastdigit))
