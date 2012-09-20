#!/usr/bin/env python

def triangle(n):
    return n * (n+1) / 2

def factor(m):
    result = 0
    for i in range(2,m-1):
        if m % i == 0:
            result += 1
    return result

x = 2
number = triangle(x)

while factor(number) < 500:
    try:
        x **= 2
        number = triangle(x)
    except MemoryError:
        print "Not enough memory for %i\n" % x
        break
print "went too far"

while factor(number) >= 500:
    x /= 2
    number = triangle(x)
print "cut back too far"

while factor(number) < 500:
    x += 1
    number = triangle(x)
print "found it"

print number
