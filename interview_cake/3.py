# Write a function fib() that a takes an integer n and returns the nth fibonacci number.

import unittest

class TestFib(unittest.TestCase):
	"""Tests the Fibonacci function."""

	def setUp(self):
		self.input_1 = 1
		self.output_1 = 1
		self.input_2 = 4
		self.output_2 = 3

	def test_prod_of_other_nums(self):
		self.assertEqual(fib(self.input_1), self.output_1)
		self.assertEqual(fib(self.input_2), self.output_2)

def fib(n):
	"""Returns the nth number in the fibonacci sequence."""

	last_2_fib_nums = [0, 1]
	for i in xrange(2, n + 1):
		two_back = last_2_fib_nums[0]
		one_back = last_2_fib_nums[1]
		last_2_fib_nums = [one_back, one_back + two_back]

	return last_2_fib_nums[-1]

if __name__ == '__main__':
	unittest.main()