def get_products_of_all_ints_except_at_index(int_array):
	"""Returns an array of the same size where each int is the product
	   of all ints not at its index."""

	products_of_all_ints_except_at_index = [1] * len(int_array)

	product = 1
	i = 0

	while i < len(int_array):
		products_of_all_ints_except_at_index[i] = product
		product *= int_array[i]
		i += 1

	product = 1
	i = len(int_array) - 1
	while i >= 0:
		products_of_all_ints_except_at_index[i] *= product
		product *= int_array[i]
		i -= 1

	return products_of_all_ints_except_at_index

print get_products_of_all_ints_except_at_index([3, 1, 2, 5, 6, 4])