# merge function

def merge(firstHalf, secondHalf, array):
	"""Inputs: three arrays of numbers - two halves to be sorted
	   									 and a third to be merged into.
	   Output: array will be the sorted, merged version of the two halves."""

	# Initialize pointers.
	i = 0
	j = 0
	k = 0

	# print "Merging %s and %s" % (firstHalf, secondHalf)

	# Use pointers to check if an entire half has already been merged.
	while i < len(firstHalf) and j < len(secondHalf):
		# If there are still numbers left, check if the left side or right
		# side is smaller. Increment the correct pointers after checking and merging.
		if firstHalf[i] < secondHalf[j]:
			array[k] = firstHalf[i]
			i += 1
		else:
			array[k] = secondHalf[j]
			j += 1
		k += 1

	# If one entire half is merged, the other half has already been sorted,
	# so it can be merged in order.
	while i < len(firstHalf):
		array[k] = firstHalf[i]
		i += 1
		k += 1

	while j < len(secondHalf):
		array[k] = secondHalf[j]
		j += 1
		k += 1

def mergeSort(array, arrays):
	"""Input: array of integers.
	   Output: sorted array of integers."""

	n = len(array)

	if n > 1:
		# print "Splitting %s" % (array)

		firstHalf = array[:n/2]
		secondHalf = array[n/2:]
		
		mergeSort(firstHalf, arrays)
		mergeSort(secondHalf, arrays)

		merge(firstHalf, secondHalf, array)


	# print "Sorted array: %s" % (array)
	arrays.append(array)

def sortedArray(array):
	arrays = []
	mergeSort(array, arrays)
	return arrays[-1]