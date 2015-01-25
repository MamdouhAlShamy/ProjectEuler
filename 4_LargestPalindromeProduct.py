#!/usr/bin/python
# A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers

def main():
	# I will start w 999 x 999
	#
	palindromList = []
	for firstNumbmer in range(999, 99, -1):
		for secondNumber in range(999, 99, -1):
			multiplyResult = firstNumbmer * secondNumber
			if isPalindromicNumber(multiplyResult):
				print( str(firstNumbmer) + " x " + str(secondNumber) + " = " + str(multiplyResult) )
				# if multiplyResult not in palindromList:
					# palindromList.append(multiplyResult)

	print(str(max(palindromList)) )
	# print(palindromList)


def isPalindromicNumber(number):
	numberList = convertNumberToList(number)
	if numberList[0] == numberList[-1] and numberList[1] == numberList[-2] and numberList[2] == numberList[-3]:
		return True



def convertNumberToList(number):
	return [int(i) for i in str(number)]

if __name__ == '__main__':
	main()