fib0 = 1
fib1 = 2
total = 2

while 1:
    fib0 += fib1
    if fib0 > 4000000:
        break
    if fib0 % 2 == 0:
        total += fib0
    fib1 += fib0
    if fib1 > 4000000:
        break
    if fib1 % 2 == 0:
        total += fib1

print total
