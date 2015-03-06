def min_diff(n, k, n_list):
	"""Given a list of n ints, returns the min. possible diff.
	   b/w max and min in a list of k ints from the list."""

	n_list.sort()
	lower = n_list[0]
	upper = n_list[k - 1]
	unfairness_min = upper - lower

	for i in xrange(1, (n - k) + 1):
		lower = n_list[i]
		upper = n_list[i + (k - 1)]
		if upper - lower < unfairness_min:
			unfairness_min = upper - lower

	return unfairness_min

import unittest

class TestMaxMin(unittest.TestCase):
	"""Class for testing the max min function."""

	def setUp(self):
		"""Initialize each test with given test data."""

		self.n_1 = 7
		self.k_1 = 3
		self.n_list_1 = [10, 100, 300, 200, 1000, 20, 30]
		self.output_1 = 20

		self.n_2 = 10
		self.k_2 = 4
		self.n_list_2 = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
		self.output_2 = 3

		self.n_3 = 6
		self.k_3 = 3
		self.n_list_3 = [10, 20, 30, 100, 101, 102]
		self.output_3 = 2

	def test_min_diff(self):
		"""Tests that the max min function returns the expected output."""

		self.assertEqual(min_diff(self.n_1, self.k_1, self.n_list_1), self.output_1)
		self.assertEqual(min_diff(self.n_2, self.k_2, self.n_list_2), self.output_2)
		self.assertEqual(min_diff(self.n_3, self.k_3, self.n_list_3), self.output_3)

if __name__ == '__main__':
	unittest.main()