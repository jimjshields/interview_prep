def two_strings(s_1, s_2):
	"""Returns boolean if s_1 and s_2 contain any identical substring."""

	return len(set(s_1).intersection(set(s_2))) > 0

import unittest

class TestTwoStrings(unittest.TestCase):

	def setUp(self):

		self.n = 2
		self.a_1 = 'hello'
		self.b_1 = 'world'
		self.a_2 = 'hi'
		self.b_2 = 'world'

	def test_two_strings(self):
		self.assertTrue(two_strings(self.a_1, self.b_1))
		self.assertFalse(two_strings(self.a_2, self.b_2))

if __name__ == '__main__':
	unittest.main()