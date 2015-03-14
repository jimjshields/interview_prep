# import unittest

# class TestStepClimbing(unittest.TestCase):

# 	def setUp(self):
# 		self.input = 10
# 		self.output = 
# 		self.input_2 = 'abc'
# 		self.output_2 = ['abc', 'bac', 'cab', 'cba', 'bca', 'acb']

# 	def test_permutations(self):
# 		self.assertEqual(sorted(permutations(self.input)), sorted(self.output))
# 		self.assertEqual(sorted(permutations(self.input_2)), sorted(self.output_2))

def climb_steps(n):
	"""Given n, return how many ways there are for 1, 2, and 3 to add to n."""

	nums = [1, 2, 3]
	for i in xrange(1, n + 1):
		for num in nums <= i:
			if 
