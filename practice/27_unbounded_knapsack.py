def closest_sum(A, k):
    """Given array A of n ints, find the closest sum of all ints to k."""
    
    sums = {0:0}
    for i in xrange(1, k + 1):
        closest = 0
        if i not in sums:
            sums[i] = 0
        for num in [a for a in A if a <= i]:
            for num_2 in [a for a in A if a <= i]:
                last_sum = sums[i - num]
                new_sum = last_sum + num_2
                if abs(k - sums[i]) > abs(k - new_sum) and new_sum <= k and new_sum <= i:
                    sums[i] = new_sum
    return sums[k]

print closest_sum([1, 6, 9], 12)
print closest_sum([3, 4, 4, 4, 8], 9)