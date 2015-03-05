import unittest

def make_change(amount, denominations):
	"""Given an amount and a list of denominations, return the number of possible combinations."""

	denominations.sort()

	num_ways = {}
	all_combos = {}
	for i in xrange(1, amount + 1):
		num_ways[i] = 0

	for a in xrange(1, amount + 1):
		combos = []
		if a in denominations:
			combos.append([a])
		for c in [c for c in denominations if c < a]:
			new = a - c
			for i in all_combos[new]:
				if sorted([c] + i) not in combos:
					combos.append(sorted([c] + i))
		all_combos[a] = combos
		num_ways[a] = len(combos)
	return num_ways
	


# class TestMakeChange(unittest.TestCase):
# 	"""Tests the make_change function."""

# 	def setUp(self):
# 		self.amount = 4
# 		self.denominations = [1, 2, 3]
# 		self.output = 4

# 	def test_make_change(self):
# 		self.assertEqual(make_change(self.amount, self.denominations), self.output)

# if __name__ == '__main__':
# 	unittest.main()





amount = 50
denominations = [1, 2, 3, 4]
output = 4

print make_change(amount, denominations)

# {0: 1, # base
#  1: 1, # [1]
#  2: 2, # [1, 1], [2]
#  3: 3, # [1, 1, 1], [2, 1], [3]
#  4: 4} # [1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1]