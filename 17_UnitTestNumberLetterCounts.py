#!/usr/bin/python

import unittest
from numberLetterCounts import NumberLetterCounts

class TestFunctions(unittest.TestCase):
	
	def testWordsUnits(self):
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(1), "one")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(5), "five")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(9), "nine")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(10), "ten")


	def testWordsTeen(self):
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(11), "eleven")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(12), "twelve")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(15), "fifteen")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(19), "nineteen")

	def testWordsUnderHundred(self):
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(20), "twenty")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(22), "twenty-two")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(27), "twenty-seven")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(31), "thirty-one")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(36), "thirty-six")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(47), "forty-seven")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(80), "eighty")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(85), "eighty-five")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(99), "ninety-nine")

	def testWordsUnderThousand(self):
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(100), "one hundred")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(101), "one hundred and one")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(211), "two hundred and eleven")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(331), "three hundred and thirty-one")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(416), "four hundred and sixteen")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(550), "five hundred and fifty")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(999), "nine hundred and ninety-nine")

	def testGivenNumbersWords(self):
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(342), "three hundred and forty-two")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(115), "one hundred and fifteen")
		self.assertEqual(NumberLetterCounts().numberToNumberInWords(1000), "one thousand")

	def testWords(self):
		self.assertEqual(NumberLetterCounts().countLettersInNumber(342), 23)
		self.assertEqual(NumberLetterCounts().countLettersInNumber(115), 20)

def main():
	unittest.main()

if __name__ == "__main__":
	main()
