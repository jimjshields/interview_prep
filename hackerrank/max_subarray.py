def max_subarray(num_list):
	"""Returns the max sum of a contiguous subarray in a given array of ints."""
	
	current_index = 0
	current_sum = 0
	best_sum = 0
	best_start_index = 0
	best_end_index = 0

	for i in xrange(len(num_list)):
		val = current_sum + num_list[i]
		if val > 0:
			if current_sum == 0:
				current_index = i
			current_sum = val
		else:
			current_sum = 0

		if current_sum > best_sum:
			best_sum = current_sum
			best_start_index = current_index
			best_end_index = i

	return sum(num_list[best_start_index:best_end_index + 1])


def max_subarray_nc(num_list):
	"""Returns the max sum of a noncontiguous subarray in a given array of ints."""
	
	num_list.sort()
	if num_list[-1] >= 0:

		# If there are any non-negative numbers, return the sum of those.
		max_sum = sum([i for i in num_list if i >= 0])
	else:

		# If not, return the negative number closest to 0.
		max_sum = num_list[-1]

	return max_sum

import unittest

class TestMaxSubArray(unittest.TestCase):
	"""Tests the max_subarray function."""

	def setUp(self):
		self.n_1 = 4
		self.list_1 = [1, 2, 3, 4]
		self.n_2 = 6
		self.list_2 = [2, -1, 2, 3, 4, -5]

		self.output_1_a = 10
		self.output_1_b = 10
		self.output_2_a = 10
		self.output_2_b = 11

	def test_max_subarray(self):
		self.assertEqual(max_subarray(self.list_1), self.output_1_a)
		self.assertEqual(max_subarray(self.list_2), self.output_2_a)

	def test_max_subarray_nc(self):
		self.assertEqual(max_subarray_nc(self.list_1), self.output_1_b)
		self.assertEqual(max_subarray_nc(self.list_2), self.output_2_b)	

if __name__ == '__main__':
	unittest.main()
