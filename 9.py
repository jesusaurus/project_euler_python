#!/usr/bin/env python

# Find a, b, c such that
#   a < b < c,
#   a + b + c = 1000,
#   a**2 + b**2 = c**2

from math import sqrt

for b in range(1,1000):
    for a in range(1, b-1):
        c = sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print "%d * %d * %d = %d", a, b, c, a*b*c
            break

