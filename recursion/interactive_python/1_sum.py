# summing a list of numbers

# brute force
a = [1, 2, 3]

def listSum(numList):
	total = 0
	for i in numList:
		total += i
	return total

# print listSum(a)

# recursive

def listSumRecursive(numList):
	if len(numList) == 1:
		return numList[0]
	else:
		print numList[0], numList[1:]
		return numList[0] + listSumRecursive(numList[1:])

print listSumRecursive(a)


# here's what's happening for the list [1, 2, 3]:
# listSumRecursive([1, 2, 3])
# len(numList) == 3
# return numList[0] + listSumRecursive(numList[1:])
# aka - return 1 + listSumRecursive([2, 3])
# -> listSumRecursive([2, 3])
# len(numList) == 2
# return numList[0] + listSumRecursive(numList[1:])
# aka - return 2 + listSumRecursive([3])
# -> listSumRecursive([3])
# len(numList) == 1
# return 3
# that 3 -> goes to listSumRecursive([3])
# -> return 2 + 3 -> return 5
# that 5 -> goes to listSumRecursive([2, 3])
# -> return 1 + 5 -> return 6
# listSumRecursive([1, 2, 3]) -> 6