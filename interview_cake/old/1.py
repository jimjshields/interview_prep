test_input = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
test_output = [(0, 1), (3, 8), (9, 12)]

test_input_2 = [(0, 1), (1, 3), (3, 5), (4, 8), (10, 12), (9, 10), (0, 12), (2, 4)]
test_output_2 = [(0, 12)]

def merge(times_array):
	"""Input: Array of 2-item-tuples representing start/end times.
	   Output: Array of 2-item-tuples representing merged start/end times for overlapping times."""

	times_array.sort(key=lambda tup: tup[0])
	# Can now assume that the first time in the tuple is always less than/equal to the first time of the next tuple.

	i = 1

	while i < len(times_array):
		current = times_array[i]
		previous = times_array[i - 1]
		if previous[1] >= current[0]:
			merged = (previous[0], max(previous[1], current[1]))
			times_array[i - 1] = merged
			del(times_array[i])
			i -= 1
		i += 1
	return times_array

import unittest

class TestMerge(unittest.TestCase):
	"""Tests the merge function."""

	def setUp(self):
		self.input = test_input
		self.input_2 = test_input_2
		self.output = test_output
		self.output_2 = test_output_2

	def test_merge(self):
		self.assertEqual(merge(self.input), self.output)
		self.assertEqual(merge(self.input_2), self.output_2)

if __name__ == '__main__':
	unittest.main()