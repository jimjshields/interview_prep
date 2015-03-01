# Shell sort - aka diminishing increment sort
# Improves on insertion sort - breaks original list into smaller sublists
# Each of which is sorted using insertion sort

# Big O:
# Worst case: O(n^2)
# Avg. case: Depends on gap selection
# Best case: O(nlog(n))
# Aux. space: O(1)

def shell_sort(a_list):
	sub_list_count = len(a_list) // 2
	while sub_list_count > 0:
		for start_position in xrange(sub_list_count):
			gap_insertion_sort(a_list, start_position, sub_list_count)

		print 'After increments of size {0}, the list is {1}.'.format(sub_list_count, a_list)

		sub_list_count //= 2

def gap_insertion_sort(a_list, start, gap):
	for i in xrange(start + gap, len(a_list), gap):
		current_value = a_list[i]
		position = i

		while position >= gap and a_list[position - gap] > current_value:
			a_list[position] = a_list[position - gap]
			position -= gap

		a_list[position] = current_value

a_list = list(range(100)[::-1])
shell_sort(a_list)
print a_list