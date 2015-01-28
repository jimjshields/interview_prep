### Utility functions ###

def splitLine(line):
	"""Input: line of comma-separated numbers
	   Output: array of integers"""

	return [int(i) for i in line.strip().split(',')]


def openFile():
	"""Input: None
	   Output: an open file with filename of the first argument"""
	import sys
	test_cases = open(sys.argv[1], 'r')
	return (splitLine(line) for line in test_cases)

### Solution functions ###
def removeDuplicates(array):
	"""Input: array of elements
	   Output: sorted array of unique elements from input array"""

	uniqueArray = []
	for n in array:
		if str(n) not in uniqueArray:
			uniqueArray.append(str(n))

	return uniqueArray

def commaSeparatedList(array):
	return ','.join(array)

for test in openFile():
	print commaSeparatedList(removeDuplicates(test))