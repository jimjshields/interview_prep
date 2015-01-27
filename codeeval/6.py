### Utility functions ###

def splitLine(line):
	"""Input: line of comma-separated numbers
	   Output: array of integers"""

	return [int(i) for i in line.strip().split(',')]

### Used Functions ###
def checkSameBits(n, pos1, pos2):
	"""Inputs: Integer n, two integers pos1 and pos2
	   pos1, pos2: positions in binary n 
	   Output: Boolean; True if the bit in pos1 is the same as that in pos2"""
	binary = str(bin(n))[2:]
	if binary[-(pos1)] == binary[-(pos2)]:
		return 'true'
	else:
		return 'false'


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	n, p1, p2 = splitLine(test)
	print checkSameBits(n, p1, p2)