### Utility functions ###
def openFile():
	import sys
	test_cases = open(sys.argv[1], 'r')
	return test_cases

### Solution functions ###
def fibSequence(n):
	"""Input: Integer n
	   Output: Array of fibonacci numbers of length n"""
	fibArray = [0, 1]
	for i in range(n):
		if i < len(fibArray):
			pass
		elif i - 2 < len(fibArray):
			fibArray.append(fibArray[i - 1] + fibArray[i - 2])
	return fibArray

def nthFib(n):
	"""Input: Integer n
	Output: Fibonacci number at position n"""
	fibArray = fibSequence(n + 1)
	return fibArray[n]

test_cases = openFile()
for test in test_cases:
	print nthFib(int(test.strip()))