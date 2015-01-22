#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def isNumberDividable(number, divider):
	if number % divider == 0:
		return True
	else:
		return False


def isEven(number):
	if number % 2 == 0:
		return True
	else:
		return False

def getPrimeFactorsOfNumber(number):
	primeList = []
	
	# get starting divider
	if isEven(number):
		divider = 2
	else:
		divider = 3

	while number != 1:
		if isNumberDividable(number, divider):
			primeList.append(divider)
			number = number / divider
		else:
			divider += 1
	print (primeList)




if __name__ == '__main__':
	getPrimeFactorsOfNumber(600851475143)