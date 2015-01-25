#!/usr/bin/python

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def getSumOfSquares(start, end):
	sumOfSquares = 0
	number = start
	while number <= end:
		sumOfSquares += number * number
		number += 1
	return sumOfSquares

def getSquareOfTheSum(start, end):
	squareOfTheSum = 0
	number = start
	while number <= end:
		squareOfTheSum += number
		number += 1
	squareOfTheSum *= squareOfTheSum
	return squareOfTheSum

if __name__ == '__main__':
	sumOfSquares = getSumOfSquares(1,100)
	print(str(sumOfSquares))

	squareOfTheSum = getSquareOfTheSum(1,100)
	print(str(squareOfTheSum))

	print( "diff: " + str(squareOfTheSum - sumOfSquares) )