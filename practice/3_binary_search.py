# Implement a binary search of a list

a_list = [i for i in xrange(1000)]

def binary_search(a_list, item):
	"""Returns a bool for whether an item is in an ordered list."""

	# Always reset the start and end indices.
	start = 0
	end = len(a_list) - 1
	# initialize a found variable - forgot this
	found = False
	
	# print "Start: {} End: {} Midpoint: {}".format(start, end, midpoint)

	while start <= end and not found:
		midpoint = (start + end) / 2
		print "Start: {}, End: {}, Midpoint: {}".format(start, end, midpoint)
		# If the midpoint is too small, re-search the second half of the list.
		if a_list[midpoint] == item:
			found = True

		if a_list[midpoint] < item:
			start = midpoint + 1

		# If the midpoint is too big, re-search the second half of the list.
		else:
			end = midpoint - 1

	return found

print binary_search(a_list, 21)