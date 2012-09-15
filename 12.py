#!/usr/bin/env python

def triangle(n):
    return sum(range(1,n))

def factor(m):
    result = []
    for i in range(2,m-1):
        if m % i == 0:
            result.append(i)
            result.extend(factor(i/m))
            return result
    return [m]

def flen(s):
    f = factor(s)
    l = len(f)
    del f
    return l

x = 10
number = triangle(x)

while flen(number) < 500:
    x **= 2
    number = triangle(x)
print "went too far"

while flen(number) >= 500:
    x /= 2
    number = triangle(x)
print "cut back too far"

while flen(number) < 500:
    x += 1
    number = triangle(x)
print "found it"

print number
