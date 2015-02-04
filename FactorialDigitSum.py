#!/usr/bin/python

#n! means n x (n - 1)  ... x 3 x 2 x 1

#For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!


class FactorialDigitSum(object):
	def factorial(self, number):
		if number == 0:
			return 1
		else:
			return number * self.factorial(number - 1)

	def convertNumberToList(self, number):
		return [int(i) for i in str(number)]

if __name__ == '__main__':
	factorialDigitalSumObject = FactorialDigitSum()
	facx = factorialDigitalSumObject.factorial(100)
	print(str(facx))
	numberList = factorialDigitalSumObject.convertNumberToList(facx)
	total = 0
	for integer in numberList:
		total += integer
	print(str(total))