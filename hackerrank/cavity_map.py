def cavity_map(n, input_map):
	"""Change any cavities in input_map to 'X' and return as list.

	n: Number of rows/columns in map.
	input_map: Map of integers given as an array of n integers (cast as strings) 
			   with n digits.

	Returns an array of strings with cavities replaced with 'X.'
	Cavity: a non-border int i where all bordering ints are < i.
	"""

	input_map = [list(line) for line in input_map]
	output_map = []

	# Only check lines not at beginning and end (non-border).
	for line_index, line in enumerate(input_map):
		new_line = []

		# Only check characters not at beginning and end (non-border).
		for n_index, num in enumerate(line):
			new_num = num
			if line_index not in [0, n - 1] and n_index not in [0, n - 1]:
				top = input_map[line_index - 1][n_index] < num
				bottom = input_map[line_index + 1][n_index] < num
				right = line[n_index + 1] < num
				left = line[n_index - 1] < num
				if top and bottom and right and left:
					new_num = 'X'
			new_line.append(new_num)
		output_map.append(new_line)


	output_map = [''.join(line) for line in output_map]

	return output_map

import unittest

class TestCavityMap(unittest.TestCase):
	"""Tests the cavity_map function w/ HR test input and output."""

	def setUp(self):
		self.n_1 = 4
		self.list_1 = ['1112', '1912', '1892', '1234']
		self.output_1 = ['1112', '1X12', '18X2', '1234']

	def test_cavity_map(self):
		self.assertEqual(cavity_map(self.n_1, self.list_1), self.output_1)

if __name__ == '__main__':
	unittest.main()
