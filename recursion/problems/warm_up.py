# naive recursive fib function

# fib_nums = [0, 1]

def fib(n, fib_nums=[1, 1]):
	if n < len(fib_nums):
		return fib_nums[n]
	else:
		f = fib(n - 1, fib_nums) + fib(n - 2, fib_nums)
		fib_nums.append(f)
		print fib_nums
		return f


# print fib(500)

# largest num in a list
def max(numbers, largest_so_far=0):
    if numbers == []:
        return largest_so_far
    next_num = numbers[0]
    if next_num > largest_so_far:
        return max(numbers[1:], largest_so_far=next_num)
    else:
        return max(numbers[1:], largest_so_far)

# print max([1, 2, 100, 4, 5, 6])

# sum of a list of numbers
def sumList(numList):
	if len(numList) == 1:
		print "Length: %s; List: %s" % (len(numList), numList)
		return numList[0]
	else:
		print "Length: %s; List: %s" % (len(numList), numList)
		return numList[0] + sumList(numList[1:])

# print sumList([1, 2, 3, 4, 5])

# last index of given input
# default return value if not found: -1
def lastIndexOf(item, itemList, lastSoFar=-1, count=0):
	# once it's gone through everything, or if it's empty,
	# return what you've found
	if itemList == []:
		return lastSoFar
	# start at the beginning
	nextItem = itemList[0]
	# next index, always
	count += 1
	if nextItem == item:
		# reset the lastSoFar - it's the index
		lastSoFar = count - 1
	# recursively call this on the smaller number set
	return lastIndexOf(item, itemList[1:], lastSoFar, count)

a = [5 for i in range(990)]
# print lastIndexOf(5, a)