# Insertion sort: 
# Worst case: O(n^2)
# Avg. case: O(n^2)
# Best case: O(n)
# Aux. Space: O(1)

# Works by maintaining a sorted sublist - each successive element inserted into that sublist

# Didn't quite get it on my own - using two loops w/ .insert() apparently doesn't work

a_list = list(range(10000)[::-1])

def insertion_sort(a_list):
	"""Sorts a list by insertion sort. Works in O(n^2) time."""

	for index in xrange(1, len(a_list)):
		current_value = a_list[index]
		position = index

		while position > 0 and a_list[position - 1] > current_value:
			a_list[position] = a_list[position - 1]
			position = position - 1

		a_list[position] = current_value

	return a_list

print insertion_sort(a_list)