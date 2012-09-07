high = 0
for x in range(100,999):
    for y in range(100,999):
        n = x * y
        string = str(n)
        if string == string[::-1] and n > high:
            high = n

print high

