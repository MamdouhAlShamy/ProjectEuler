#!/usr/bin/python


#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def getSmallestNumber():
	#get number
	#isItDividableBy()
	# 11645854
	number = 20522266				
	while True:
		if isSmallestDivisbleBy1To20(number):
			return number
		# print(str(number))
		number += 1	

def isSmallestDivisbleBy1To20(number):
	divider = 20
	while divider != 1:
		if number % divider != 0:
			return False
		else:
			divider -= 1
	print(str(number))
	return True

def test(number):
	for i in range(1, 21):
		if number % i == 0 :
			pass
		else:
			print ("False")
			return
	print ("TRUE NUMBER")


if __name__ == '__main__':
	# n = getSmallestNumber()
	# print("smallest number: " + str(n) )
	test(232792560)