print 'HELLO'
# print 3%2

## I want to get prime numbers under 10
## 2 is the only even number in prime numbers

primeNumbers = []

def isItDividableBy(n, divider):
	# print "n: " + str(n) + ", divider: " + str(divider)
	if(n % divider == 0):
		return 1
	return 0

def isItPrime(n):
	if not not primeNumbers: # not empty list case
		for p in primeNumbers:
			if (n != p): # not divided by itself
				if isItDividableBy(n,p):
					return 0
		primeNumbers.append(n)
	else: # populate empty list
		primeNumbers.append(n)
		return 1


for number in range(2, 2000000):
	isItPrime(number)

print sum(primeNumbers)
print "DONE"