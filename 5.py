num = 21
while True:
    for i in range(1,20):
        if num % i != 0:
            num += 1
            break
    else:
        print num
        break
