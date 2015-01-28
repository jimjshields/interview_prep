# attempt at implementation of quicksort

def quickSort(array):
	if len(array) == 1:
		return array
	else:
		print "Partitioning %s" % (array)
		pivot = partition(array)
		print "Pivot: %s" % (pivot)
		quickSort(array[:pivot])
		quickSort(array[pivot + 1:])

	return array

def partition(array):
	pivot = array.pop(0)

	print "Pivot: %s" % (pivot)
	print "Array: %s" % (array)

	# pointer for pivot
	i = 0

	for n, item in enumerate(array):
		if item < pivot:
			print "Swapping %s and %s" % (pivot, item)
			array[i] = item
			i += 1
		else:
			array.append(array.pop(n))

	array.insert(i + 1, pivot)

	print "Pivoted array: %s" % (array)

	return i

a = [3, 2, 5, 1, 2, 4]
print quickSort(a)