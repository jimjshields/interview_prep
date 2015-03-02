# Implement a function to convert a number from base 10 to any base
# Forgot - check if less than base in the front (return digit if so)
# And divide by to_base, not by 2

def convert_base(num, to_base):
	"""Given a base 10 number, convert to any base from 2 to 16."""

	digits = '0123456789ABCDEF'
	res = ''

	if num < to_base:
		return digits[num]
	elif num >= to_base:
		new_num = num // to_base
		rem = num % to_base
		return convert_base(new_num, to_base) + digits[rem]

	return res