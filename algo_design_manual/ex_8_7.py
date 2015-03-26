"""
In the United States, coins are minted with denominations of 1, 5, 10, 25,
and 50 cents. Now consider a country whose coins are minted with denominations
of {d1,...,dk} units. We want to count how many distinct ways C(n) there are
to make change of n units. For example, in a country whose denominations are
{1, 6, 10}, C(5) = 1, C(6) to C(9) = 2, C(10) = 3, and C(12) = 4.
"""

def coin_combos(amt, denoms):
	coin_combos = {0:1}

	for a in xrange(1, amt + 1):
		for c in [coin for coin in denoms if coin <= a]:
			if a not in coin_combos:
				coin_combos[a] = 1
			else:
				coin_combos[a] += coin_combos[a - c]

	return coin_combos

import pprint
pprint.pprint(coin_combos(20, [1, 6, 10]))
