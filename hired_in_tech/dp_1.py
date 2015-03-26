# Given a list of N ordered integers find the longest increasing subsequence in this list. Example: If the list is [16, 3, 5, 19, 10, 14, 12, 0, 15] one possible answer is the subsequence [3, 5, 10, 12, 15], another is [3, 5, 10, 14, 15].

# Solve using dynamic programming.
# Constraints: array of unsigned ints. Find the longest increasing subsequence.
# N: len(array); solve for N <= 2,000,000

# Ideas:
# Recursion: Start at end and recurse for the rest
# Dynamic programming: Calculate for smallest state (0 ints) and store; access in dict for next calc

a = [16, 3, 5, 19, 10, 14, 12, 0, 15]
answer_1 = [3, 5, 10, 12, 15]
answer_2 = [3, 5, 10, 14, 15]

def lis(int_array):
	"""Given an array of ints, return the longest increasing subsequence (lis)."""

	longest = {0:[], 1:[[int_array[0]]]}

	for i in xrange(2, len(int_array) + 1):
		if int_array[i] < int_array[i - 1]:
			if longest[i - 1][-1] > int_array[i]:
				longest[i] = longest[i - 1][:-1] + [int_array[i]]
