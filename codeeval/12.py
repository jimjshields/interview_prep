def oddNumbers(max):
	"""Input: integer
	   Output: array of odd numbers below max"""

	numRange = (n for n in range(1, max + 1))
	return (n for n in numRange if n % 2 != 0)

for n in oddNumbers(99):
	print n