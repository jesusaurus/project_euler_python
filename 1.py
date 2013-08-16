#!/bin/python

def _gen(n):
    x = 0
    while x < n:
        if (x % 3 == 0) or (x % 5 == 0):
            yield x
        x += 1


total = 0
for x in _gen(1000):
        total += x

print total
