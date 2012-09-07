import math

magick = 600851475143

#initial set of primes
primes = [ 2, 3, 5, 7 ]

def factor(n):
    factors = []
    primes = []

    for x in range(2,n):
        if n > x and n % x == 0:
            factors.append(x)

    if factors:
        for i in factors:
            primes.extend(factor(i))
    else:
        primes.append(n)

    return primes

print factor(magick)
