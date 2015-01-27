### Utility functions ###

def splitLine(line):
	"""Input: line of comma-separated numbers
	   Output: array of integers"""

	return [int(i) for i in line.strip().split(',')]


def openFile():
	import sys
	test_cases = open(sys.argv[1], 'r')
	return test_cases