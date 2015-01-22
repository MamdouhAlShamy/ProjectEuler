#!/usr/bin/python

# Multiples of 3 and 5

def isNumberMultipleOfBase(base, number):
	if number%base == 0:
		return True
	else:
		return False

def getMultiplesOf(base, stoppingNumber):
	sum = 0
	for i in range(1,stoppingNumber):
		if isNumberMultipleOfBase(base, i):
			# print ("Number " + str(i) + " is multiple of " + str(base) )
			sum += i
	return sum

def getMultiplesOf(base1,base2, stoppingNumber):
	sum = 0
	for number in range(1,stoppingNumber):
		if isNumberMultipleOfBase(base1, number):
			# print ("Number " + str(i) + " is multiple of " + str(base) )
			sum += number
		elif isNumberMultipleOfBase(base2, number):
			sum += number
	return sum

if __name__ == '__main__':
	# sum3 = getMultiplesOf(3,1000)
	# print ("Sum of 3 is " + str(sum3) )
	# sum5 = getMultiplesOf(5,1000)
	# print ("Sum of 5 is " + str(sum5) )
	# sumt = sum3 + sum5
	# print("Total sum: " + str(sumt) )

	sumt = getMultiplesOf(3, 5, 1000)
	print("Total sum: " + str(sumt) )

## Wut I learned in this ex. 
## 1) using Intention-revealing func
## 2) dividing func to smaller parts function
## 3) small twist in function can reduce looping