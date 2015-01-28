def openFile():
	import sys
	test_cases = open(sys.argv[1], 'r')
	return test_cases

test_cases = openFile()

total = 0
for i in test_cases:
	total += int(i)
print total