#!/usr/bin/python



# The following iterative sequence is defined for the set of positive integers:

# n  n/2 (n is even)
# n  3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13  40  20  10  5  16  8  4  2  1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.



def isNumberEven(number):
	if number % 2 == 0:
		return True
	else:
		return False

def countCollatzSequance(number):
	count = 1
	# seq = [number]
	while number != 1:
		if isNumberEven(number):
			number = number / 2
		else:
			number = number * 3 + 1
		count += 1
		# seq.append(number)
	return count

if __name__ == '__main__':
	# number = 13
	# count,seq = countCollatzSequance(number)
	# print(str(number) + " generated " + str(count) + " terms  seq: " + str(seq) )

	iterator = 13
	maxCount = 0
	maxNumber = 0
	while iterator < 1000000:
		count = countCollatzSequance(iterator)
		if count > maxCount:
			maxCount = count
			maxNumber = iterator
		iterator += 1

	print("maxNumber: " + str(maxNumber) + " maxCount: " + str(maxCount) )

