import unittest

class TestStockPrices(unittest.TestCase):
	"""Tests the stock prices function."""

	def setUp(self):
		self.input = [1, 2, 3]
		self.output = 2
		self.input_2 = [2, 3, 1, 6, -1, 2]
		self.output_2 = 5

	def test_stock_prices(self):
		self.assertEqual(stock_prices(self.input), self.output)

def stock_prices(stock_prices_array):
	"""Returns the maximum profit from one buy and one sell of stock at 
	   prices in the given array."""

	# Initialize price diff array with a 0 at the start, should mirror the
	# stock_prices_array.
	price_diffs = [0]

	# Add the price diffs minute-over-minute to that array.
	for i in xrange(len(stock_prices_array) - 1):
		price_diffs.append(stock_prices_array[i + 1] - stock_prices_array[i])

	# Start w/ the assumption that
	# the max profit you can make is buying at minute 0 and selling at
	# the last minute.
	start = 0
	end = len(price_diffs) - 1
	max_sum = sum(price_diffs)

	# Walk through the price diffs array. You only have to do n/2 checks,
	# b/c you started at the outsides and systematically work your way in.
	while start < end:
		if sum(price_diffs[start + 1:]) > sum(price_diffs[:end]):
			start += 1
			if sum(price_diffs[start + 1:]) > max_sum:
				max_sum = sum(price_diffs[start + 1:])
		else:
			end -= 1
			if sum(price_diffs[:end]) > max_sum:
				max_sum = sum(price_diffs[:end])

	return max_sum

# Other way - IC's way.

def get_best_profit(stock_prices_array):
	min_price = stock_prices_array[0]
	max_profit = 0

	for current_price in stock_prices_array:
		min_price = min(current_price, min_price)
		max_profit = max(current_price - min_price, max_profit)

	return max_profit

if __name__ == '__main__':
	unittest.main()


[0, 1, 1]