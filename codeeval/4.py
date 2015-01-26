def reverseWords(line):
	line = ' '.join(line.strip().split(' ')[::-1])
	return line
	
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	print reverseWords(test)

test_cases.close()