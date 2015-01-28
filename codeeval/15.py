### Utility functions ###

def splitLine(line, delimiter):
	"""Input: line of comma-separated numbers
	   Output: array of integers"""

	return [i for i in line.strip().split(delimiter)]

def openFile():
	"""Input: None
	   Output: an open file with filename of the first argument"""
	import sys
	test_cases = open(sys.argv[1], 'r')
	return (line for line in test_cases)

tests = []

for test in openFile():
	tests.append(splitLine(test, ';'))
	print test
	# for numSet in test:
		# print numSet
		# numSet = list(numSet)
		# splitLine(numSet, ';')

# print tests
