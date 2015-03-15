import unittest

class TestStockPrices(unittest.TestCase):
	"""Tests the stock prices function."""

	def setUp(self):
		self.input = [1, 7, 3, 4]
		self.output = [84, 12, 28, 21]
		self.input_2 = [1, 2, 6, 5, 9]
		self.output_2 = [540, 270, 90, 108, 60]

	def test_prod_of_other_nums(self):
		self.assertEqual(prod_of_other_nums(self.input), self.output)
		self.assertEqual(prod_of_other_nums(self.input_2), self.output_2)

def prod_of_other_nums(num_list):
	"""Given a list of ints, returns a list of ints where each int is the
	   product of every other int in the list."""

	# Edge cases: 0 or one elements.
	if num_list == []:
		return []
	elif len(num_list) == 1:
		return [1]

	# Build an array of products of nums before each item. Start w/ 1
	# as there's nothing before the first item in the list.

	prod_array = [1]
	current_prod = 1
	i = 1

	# Walk through num_list and append the product of all nums before 
	# each num.
	while i < len(num_list):

		# Multiply by the item before it in the list.
		current_prod *= num_list[i - 1]
		prod_array.append(current_prod)
		i += 1

	# Now do it backwards - walk from the end to the beginning and
	# multiply each prod in prod_array by all nums after each num in num_list.
	
	current_prod = 1
	i = len(num_list) - 2

	while i >= 0:

		# Multiply by the item after it in the list.
		current_prod *= num_list[i + 1]
		prod_array[i] *= current_prod
		i -= 1

	return prod_array


if __name__ == '__main__':
	unittest.main()