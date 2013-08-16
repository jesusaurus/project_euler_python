def _fib():
    fib0 = 1
    yield fib0
    fib1 = 2
    yield fib1

    while True:
        fib0 += fib1
        yield fib0
        fib1 += fib0
        yield fib1


def fib(x):
    for f in _fib():
        if f > x:
            break
        elif f % 2 == 0:
            yield f


print sum(fib(4000000))
