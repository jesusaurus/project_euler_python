#!/usr/bin/env python

def triangle(n):
    return n * (n+1) / 2

def factor(m):
    result = 0
    i = 2
    while i < (m-1):
        if m % i == 0:
            result += 1
        i += 1
    return result

x = 2
number = triangle(x)

try:
    while factor(number) < 500:
        x **= 2
        number = triangle(x)
    print "went too far"
except MemoryError:
    print "Not enough memory for %i\n" % x

while factor(number) >= 500:
    x /= 2
    number = triangle(x)
print "cut back too far"

while factor(number) < 500:
    x += 1
    number = triangle(x)
print "found it"

print number
