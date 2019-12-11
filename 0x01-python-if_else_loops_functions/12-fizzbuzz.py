#!/usr/bin/python3
for i in range(1, 101):
    if i != 100:
        print('Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i), end=" ")
    else:
        print('Fizz ' * (not i % 3) + 'Buzz ' * (not i % 5) or str(i))
