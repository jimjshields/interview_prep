### Utility functions ###
def openFile():
	import sys
	test_cases = open(sys.argv[1], 'r')
	return test_cases

test_cases = openFile()
for test in test_cases:
	print test.strip().lower()