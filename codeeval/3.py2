def isPrime(num):
	"""Input: Any integer
	   Output: Boolean for whether the number is prime"""

	if num == 2:
		return True

	if num % 2 == 0:
		return False

	for i in range(3, num/2 + 1):
		if num % i == 0:
			return False

	else:
		return True

primesArray = []

for i in range(2, 10000, 1):
	if len(primesArray) < 1000:
		if isPrime(i):
			primesArray.append(i)

print sum(primesArray)