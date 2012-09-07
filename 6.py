sumOfSquares = 0
squareOfSums = 0

for i in range (1,101):
    squareOfSums += i
    sumOfSquares += (i ** 2)

squareOfSums = squareOfSums ** 2

print squareOfSums - sumOfSquares
