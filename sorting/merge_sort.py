def mergeSort(array):
	"""Input: array/list of comparable items
	   Output: sorted array/list of items"""

	n = len(array)

	if n > 1:
		firstHalf = array[:n/2]
		secondHalf = array[n/2:]
		mergeSort(firstHalf)
		mergeSort(secondHalf)
		merge(firstHalf, secondHalf, array)

	return array

def merge(firstHalf, secondHalf, array):
	"""Input: Three lists, the first two are sorted halves of the third
	   Output: The third array has been sorted in place by merging 
	   		   the sorted first and second halves"""

	i = 0
	j = 0
	k = 0

	while i < len(firstHalf) and j < len(secondHalf):
		if firstHalf[i] < secondHalf[j]:
			array[k] = firstHalf[i]
			i += 1
		else:
			array[k] = secondHalf[j]
			j += 1
		k += 1

	while i < len(firstHalf):
		array[k] = firstHalf[i]
		i += 1
		k += 1

	while j < len(secondHalf):
		array[k] = secondHalf[j]
		j += 1
		k += 1

a = [i for i in range(100000, 0, -1)]
print mergeSort(a)