### Utility functions ###
def openFile():
	import sys
	test_cases = open(sys.argv[1], 'r')
	return test_cases

### Solution functions ###
def sumOfDigits(num):
	num = str(num)
	if len(num) == 1:
		return int(num)
	else:
		return int(num[0]) + sumOfDigits(num[1:])


test_cases = openFile()
for test in test_cases:
	print sumOfDigits(test.strip())