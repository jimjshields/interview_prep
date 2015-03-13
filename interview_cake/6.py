def radix_sort(num_list, max_num):
	RADIX = 10
	tmp, placement = -1, 1

	while placement < max_num:
		buckets = [[] for _ in xrange(RADIX)]
		for i in num_list:
			tmp = i / placement
			buckets[tmp % RADIX].append(i)
		num_list = []
		for b in buckets:
			for num in b:
				num_list.append(num)
		placement *= 10

	return num_list

import timeit

print timeit.timeit('radix_sort(num_list, 10000)', 'from __main__ import radix_sort; num_list = [i for i in xrange(10000)][::-1]', number=100)
print timeit.timeit('num_list.sort()', 'from __main__ import radix_sort; num_list = [i for i in xrange(10000)][::-1]', number=100)

# import unittest

# class TestSortFinite(unittest.TestCase):
# 	"""Tests that our function returns an array of all possible permutations."""

# 	def setUp(self):
# 		self.input_1 = [50, 1, 3, 4, 2]
# 		self.output_1 = [1, 2, 3, 4, 50]

# 		self.input_2 = [1, 3, 4, 2, -50]
# 		self.output_2 = [-50, 1, 2, 3, 4]

# 	def test_permutations(self):
# 		self.assertEqual(permutations(self.input_1), self.output_1)
# 		self.assertUnequal(permutations(self.input_2), self.output_2)

# if __name__ == '__main__':
# 	unittest.main()