#!/usr/bin/python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def isNumberPrime(number):
	# if number == 2: return True
	divider = 2
	while divider != number:
		if number % divider == 0:
			return False
		else:
			divider += 1
	return True

def sumOfAllPrimesBelow(n):
	number = 3
	sum = 0
	while number < n:
		if isNumberPrime(number):
			sum += number
		number += 1
	return sum


def isItDividableBy(number, divider):
	if number % divider == 0:
		return True
	return False

def isNumberPrimeModified(number, primeList):
	for p in primeList:
		if isItDividableBy(number,p):
			return False
	return True
			

def sumOfAllPrimesBelowModified(n):
	number = 3
	total = 2
	primeList = [2]
	while number < n:
		if isNumberPrimeModified(number, primeList):
			primeList.append(number)
			total += number
		number +=1
		# print(primeList)
	return total



if __name__ == '__main__':
	total = sumOfAllPrimesBelowModified(2000000)
	print (str(total))