#!/usr/bin/python



#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?


def getTheNthPrimeNumber(n):
	primeLocation = 0
	number = 2
	while primeLocation < n:
		if isNumberPrime(number):
			primeLocation += 1
		number += 1

	print (str(number-1))

def isNumberPrime(number):
	divider = 2
	while divider != number:
		if number % divider == 0:
			return False
		else:
			divider += 1
	return True


if __name__ == '__main__':
	getTheNthPrimeNumber(10001)
