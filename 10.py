import math

#initial set of primes
primes = [ 2, 3, 5, 7, 11 ]

def findPrimes(m):
    while primes[-1] < m:
        last = primes[-1]
        for x in range(last+1, last*2):
            f = factor(x)
            if len(f) == 1:
                primes.extend(f)
        print "number of primes found: ",
        print len(primes)
        print "last prime: ",
        print primes[-1]
        print

def factor(n):
    result = []

    for p in primes:
        if n > p and n % p == 0:
            result.append(p)
            result.extend(factor(n/p))
            return result

    return [n]

findPrimes(2000000)
print sum(primes)
