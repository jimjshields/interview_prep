def merge_sort(array):
	"""Recursively sorts an array of comparable items."""

	n = len(array)

	if n > 1:
		first_half = array[:n/2]
		second_half = array[n/2:]

		merge_sort(first_half)
		merge_sort(second_half)

		merge(array, first_half, second_half)

	return array


def merge(array, first_half, second_half):
	"""Merges the first and second half of an array."""

	i = 0
	j = 0
	k = 0

	# Run through the two halves, adding the lower number to the array.
	while i < len(first_half) and j < len(second_half):
		if first_half[i] < second_half[j]:
			array[k] = first_half[i]
			i += 1
		else:
			array[k] = second_half[j]
			j += 1

		k += 1

	# If you're done w/ the second half you can just run through the first half - it's already sorted.

	while i < len(first_half):
		array[k] = first_half[i]

		i += 1
		k += 1

	# If you're done w/ the first half you can just run through the second half - it's already sorted.
	while j < len(second_half):
		array[k] = second_half[j]

		j += 1
		k += 1