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

	return res

class TestScrabbleWords(unittest.TestCase):

	def setUp(self):
		self.input = 'ab'
		self.output = ['ab', 'ba', 'a', 'b']
		self.input_2 = 'abc'
		self.output_2 = ['abc', 'bac', 'cab', 'cba', 'bca', 'acb', 'ac', 'ab', 'ba', 'bc', 'ca', 'cb', 'a', 'b', 'c']

	def test_scrabble_words(self):
		self.assertEqual(sorted(scrabble_words(self.input)), sorted(self.output))
		self.assertEqual(sorted(scrabble_words(self.input_2)), sorted(self.output_2))

def scrabble_words(letters):
	"""Returns all permutations of all combinations of a given set of letters."""

	res = []
	length = len(letters)

	if length <= 1:
		res = [letters]
	else:
		for i, c in enumerate(letters):
			for scrabble_word in scrabble_words(letters[:i] + letters[i + 1:]):
				if letters[i] + scrabble_word not in res:
					res.append(letters[i] + scrabble_word)
				if scrabble_word not in res:
					res.append(scrabble_word)
	return res

if __name__ == '__main__':
	unittest.main()