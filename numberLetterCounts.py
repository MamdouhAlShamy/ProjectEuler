#!/usr/bin/python

#If the numbers 1 to 5 are written out in words: one, two, three, four, five
#, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
#how many letters would be used?

#NOTE: Do not count spaces or hyphens. 
#For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

class NumberLetterCounts(object):

	def getNumberUnitsInWords(self, numberUnits):
	    return {
	        1: "one",
	        2: 'two',
	        3: "three",
	        4: "four",
	        5: "five",
	        6: "six",
	        7: "seven",
	        8: "eight",
	        9: "nine",
	    }[numberUnits]

	def getNumberTensInWords(self, numberTens):
	    return {
	        1: "ten",
	        2: 'twenty',
	        3: "thirty",
	        4: "forty",
	        5: "fifty",
	        6: "sixty",
	        7: "seventy",
	        8: "eighty",
	        9: "ninety",
	    }[numberTens]

	def getNumberHundredsInWords(self, numberHundreds):
	    return {
	        1: "one hundred",
	        2: "two hundred",
	        3: "three hundred",
	        4: "four hundred",
	        5: "five hundred",
	        6: "six hundred",
	        7: "seven hundred",
	        8: "eight hundred",
	        9: "nine hundred",
	    }[numberHundreds]

	def getNumberTeensInWords(self, numberTeens):
		    return {
		    10: "ten",
	        11: "eleven",
	        12: "twelve",
	        13: "thirteen",
	        14: "fourteen",
	        15: "fifteen",
	        16: "sixteen",
	        17: "seventeen",
	        18: "eighteen",
	        19: "nineteen",
	    }[numberTeens]

	def convertNumberToList(self, number):
		return [int(i) for i in str(number)]

	def numberToNumberInWords(self, number):
		numberInWords = ""
		numberList = self.convertNumberToList(number)

		# 1 - 9
		if number < 10:
			numberInWords += self.getNumberUnitsInWords(number)
		
		# 10 -19
		elif number < 20:
			numberInWords += self.getNumberTeensInWords(number)

		# 20 - 99
		elif number < 100:
			tens = numberList[0]
			units = numberList[1]
			numberInWords += self.getNumberTensInWords(tens)
			if units != 0:
				numberInWords += "-"
				numberInWords += self.getNumberUnitsInWords(units)
		
		# 100 - 999
		elif number < 1000:
			hundreds = numberList[0]
			tens = numberList[1]
			units = numberList[2]

			numberInWords += self.getNumberHundredsInWords(hundreds)
			if tens == 0:
				if units != 0:
					numberInWords += " and "
					numberInWords += self.getNumberUnitsInWords(units)
			elif tens == 1:
				numberInWords += " and "
				number = tens * 10 +  units
				numberInWords += self.getNumberTeensInWords(number)
			else:
				numberInWords += " and "
				numberInWords += self.getNumberTensInWords(tens)
				if units != 0:
					numberInWords += "-"
					numberInWords += self.getNumberUnitsInWords(units)

		# 1000
		else:
			numberInWords += "one thousand"

		# Hundred and above
		return numberInWords

	def countLetter(self, text):
		return len(text) - text.count(' ') - text.count('-')

	def countLettersInNumber(self, number):
		words = self.numberToNumberInWords(number)
		return self.countLetter(words)


if __name__ == '__main__':
	total = 0
	numberLettersCountsObject = NumberLetterCounts()
	for number in range(1,1001):
		print(str(number))
		total += numberLettersCountsObject.countLettersInNumber(number)

	print("Total number of letters from 1 to 1000: " + str(total) )
