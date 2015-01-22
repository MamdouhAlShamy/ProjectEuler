#!/usr/bin/python

# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding 
# the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million
# , find the sum of the even-valued terms.


def fibonacciSeriesGenerator(stoppingNumber):
	seed = 1
	sum = 2
	result = "1,2"
	while sum < stoppingNumber:
		temp = sum + seed
		seed = sum
		sum = temp
		if sum < stoppingNumber:
			result += ", " + str(sum)
	print(result)

def isNumberEven(number):
	if number % 2 == 0:
		return True
	else:
		return False

def sumEvenFibonacciSeries(stoppingNumber):
	first = 1
	second = 2
	total = 2 
	while second < stoppingNumber:
		temp = second + first
		first = second
		second = temp
		if second <= stoppingNumber:
			if isNumberEven(second):
				total += second
			# print(", " + str(second))
	return total

if __name__ == '__main__':
	#fibonacciSeriesGenerator(4000000)

	total = sumEvenFibonacciSeries(4000000)
	print ("Total: " + str(total))