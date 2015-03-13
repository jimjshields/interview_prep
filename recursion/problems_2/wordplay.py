import unittest

class TestPermutations(unittest.TestCase):

	def setUp(self):
		self.input = 'ab'
		self.output = ['ab', 'ba']
		self.input_2 = 'abc'
		self.output_2 = ['abc', 'bac', 'cab', 'cba', 'bca', 'acb']

	def test_permutations(self):
		self.assertEqual(sorted(permutations(self.input)), sorted(self.output))
		self.assertEqual(sorted(permutations(self.input_2)), sorted(self.output_2))

def permutations(word):
	"""Returns a set of all permutations of a given word."""

	length = len(word)
	res = []
	
	if length <= 1:
		res = [word]
	else:
		for c_index in xrange(length):
			for perm in permutations(word[:c_index] + word[c_index + 1:]):
				res.append(word[c_index] + perm)

	print word, res			# perms.add(word[c_index] + perm)
	return res

if __name__ == '__main__':
	unittest.main()