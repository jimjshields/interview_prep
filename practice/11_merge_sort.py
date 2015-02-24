# Implementing merge sort
# Concepts: Recursion, divide & conquer
# Remember: need two separate function (merge_sort and merge)
# Careful - pay attention to details (splitting list in half)

def merge_sort(a_list):
	"""Returns a sorted list of comparable items."""

	n = len(a_list)

	if n > 1:

		first_half = a_list[:n/2]
		second_half = a_list[n/2:]

		merge_sort(first_half)
		merge_sort(second_half)

		merge(first_half, second_half, a_list)

	return a_list

def merge(first_half, second_half, array):
	"""Merges the first and second half of an array."""

	i = 0
	j = 0
	k = 0

	while i < len(first_half) and j < len(second_half):
		if first_half[i] < second_half[j]:
			array[k] = first_half[i]
			i += 1
		else:
			array[k] = second_half[j]
			j += 1
		k += 1

	while i < len(first_half):
		array[k] = first_half[i]
		i += 1
		k += 1

	while j < len(second_half):
		array[k] = second_half[j]
		j += 1
		k += 1

a_list = [i for i in xrange(1000)][::-1]
print merge_sort(a_list)