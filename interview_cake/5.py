# Making Change

# Given an amount and list of coin denominations, return the number of ways
# you can make amount w/ the denominations.

import unittest

class TestMakeChange(unittest.TestCase):
	"""Tests the make_change function."""

	def setUp(self):
		self.amount_1 = 4
		self.denoms_1 = [1, 2, 3]
		self.output_1 = 4

	def test_make_change(self):
		self.assertEqual(make_change(self.amount_1, self.denoms_1), self.output_1)

def make_change(amount, denoms):
	"""Given an amount and a list of denominations, returns the number of ways
	   the amount can be made."""

	ways_of_doing_n_cents = [0] * (amount + 1)
	ways_of_doing_n_cents[0] = 1

	for coin in denoms:
		for higher_amount in xrange(coin, amount + 1):
			higher_amount_remainder	= higher_amount - coin
			ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
	return ways_of_doing_n_cents[amount]

if __name__ == '__main__':
	unittest.main()