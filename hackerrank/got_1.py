def palindrome_anagram(string):
	"""Given a string, returns a boolean for whether any anagram of
	   that string can be a palindrone."""

	length = len(string)
	
	# Case 1: 1-letter strings are always palindromic.
	if length == 1: return True

	# Note: takes O(nlog(n)) time but no additional space
	string_list = sorted(list(string))
	
	odd_count = 0
	i = 0
	next = 1

	while next < length:
		if string_list[i] == string_list[next]:
			i += 2
			next += 2
		else:
			odd_count += 1
			i += 1
			next += 1
		if odd_count > 1: return False

	return True


import unittest

class TestPalindromeAnagram(unittest.TestCase):
	"""Tests a function for determining whether an anagram of a string 
	   can be a palindrone."""

	def setUp(self):
		self.input_1 = 'aaabbbb'

		self.input_2 = 'cdefghmnopqrstuvw'

		self.input_3 = 'cdcdcdcdeeeef'

	def test_palindrome_anagram(self):
		self.assertTrue(palindrome_anagram(self.input_1))
		self.assertFalse(palindrome_anagram(self.input_2))
		self.assertTrue(palindrome_anagram(self.input_3))

if __name__ == '__main__':
	unittest.main()