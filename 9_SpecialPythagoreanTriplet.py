#!/usr/bin/python



#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def isPythagoreanTriplets(a,b,c):
	if ((a*a) + (b*b)) == (c*c) and a < b < c :
		return True
	return False

def isEqualSummationEq1000(a,b,c):
	if a+b+c == 1000:
		return True
	return False

def main():
	for a in range(2, 1000):
		for b in range(3,1000):
			for c in range(4,1000):
				if isPythagoreanTriplets(a,b,c) and isEqualSummationEq1000(a,b,c):
					print ("a: " + str(a) + " b: " + str(b) + " c: " + str(c))
					return a*b*c


if __name__ == '__main__':
	import time
	startTime = time.time()
	n = main()
	print("--- %s seconds ---" % time.time() - start_time)
	print("result " + str(n) )
