# Implement a bubble sort

a = [i for i in xrange(1000)][::-1]

def bubble_sort(a_list):
	"""Sorts a comparable list w/ bubble sort."""

	for n in range(len(a_list)):
		for i in range(1, len(a_list)):
			if a_list[i] < a_list[i - 1]:
				a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]
				print "Swapping {} and {}".format(a_list[i - 1], a_list[i])

	return a_list

print bubble_sort(a)