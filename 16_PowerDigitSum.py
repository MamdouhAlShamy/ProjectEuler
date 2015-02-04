#!/usr/bin/python

def getNumberToThePower(number, power):
	times = 1
	result = number
	while times < power:
		 result *= 2
		 times += 1
	print(str(result))
	return result

def convertNumberToList(number):
	return [int(i) for i in str(number)]

def sumList(numberlist):
	total = 0
	for number in numberlist:
		total += number
	return total

if __name__ == '__main__':
	twoOneHunderdTimes = getNumberToThePower(2, 1000)
	numberAsList = convertNumberToList(twoOneHunderdTimes)
	total = sumList(numberAsList)
	print("total: " + str(total))