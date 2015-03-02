# Three rules of recursion
# 1. Function must always have a base case - a way for the algorithm to escape/return a value
# 2. Function must be moving toward the base case
# 3. Function must always call itself recursively

# Simplest recursive example - fibonacci

def fibonacci(max_num):
	"""Gives the fibonacci number at max_num in the sequence, starting at 0."""

	# base case
	if max_num <= 1:
		return 1
	else:
		# moving toward base case
		# calling itself recursively
		return fibonacci(max_num - 1) + fibonacci(max_num - 2)

# More complex - convert base

def convert_base(num, to_base):
	"""Converts a base 10 number to a given base up to 16 
	   and returns the result as a string."""

	digits = '0123456789ABCDEF'
	result = ''

	if num < to_base:
		return digits[num]
	else:
		result += convert_base(num/to_base, to_base) + str(digits[num % to_base])

	return result

def fibonacci(max_num):
	if max_num <= 1:
		return 1
	else:
		return fibonacci(max_num - 1) + fibonacci(max_num - 2)
