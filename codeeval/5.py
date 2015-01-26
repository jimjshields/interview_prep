def splitLine(line):
	"""Input: line of comma-separated numbers
	   Output: array of integers"""

	return [int(i) for i in line.strip().split(',')]

def firstMultipleAboveMax(n, max):
	"""Inputs: An integer n and a maximum integer
	   Output: The first multiple of n above the max"""
	
	# all multiples below the max (stupid for now, preset num of multiples)
	multiples = [i for i in range(1000) if n * i < max]
	# return the next one after the one under the max
	return n * (multiples[-1] + 1)

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	x, n = splitLine(test)
	print firstMultipleAboveMax(n, x)