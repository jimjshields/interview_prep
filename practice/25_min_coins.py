denoms = [1, 3, 5]
n = 11

def min_coins(n, denoms):
	"""Finds the min number of denom coins to make n."""

	min_dict = {0:0}

	for amt in xrange(1, n + 1):
		# Init at i coins, always the maximum if min(denoms) >= 1.
		min_coins = amt
		for coin in (coin for coin in denoms if coin <= amt):
			if amt not in min_dict:
				min_dict[amt] = min_dict[amt - coin] + 1
			elif min_dict[amt - coin] + 1 < min_coins:
				min_dict[amt] = min_dict[amt - coin] + 1
			min_coins = min_dict[amt]
	print min_dict
	return min_dict[n]

print min_coins(n, denoms)