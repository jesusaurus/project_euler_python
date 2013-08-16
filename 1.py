#!/bin/python

def _gen(n):
    x = 0
    while x < n:
        if (x % 3 == 0) or (x % 5 == 0):
            yield x
        x += 1

print sum(_gen(1000))
