def permutations(string, length):
	"""Returns all permutations of a given string, with dupes."""

	last_char = string[-1]
	all_chars_but_last = string[:-1]

	if len(string) <= 1:
		return string
	else:
		for i, c in enumerate(string):
			for perm in permutations(string[:i] + string[i + 1:], len(string)):
				return c + perm

# import unittest

# class TestPermutations(unittest.TestCase):
# 	"""Tests that our function returns an array of all possible permutations."""

# 	def setUp(self):
# 		self.input_1 = 'ab'
# 		self.output_1 = ['ab', 'ba']

# 		self.input_2 = 'abc'
# 		self.output_2 = ['abc', 'bac']

# 	def test_permutations(self):
# 		self.assertEqual(permutations(self.input_1), self.output_1)
# 		self.assertUnequal(permutations(self.input_2), self.output_2)

# if __name__ == '__main__':
# 	unittest.main()