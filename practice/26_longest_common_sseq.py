a = [1, 2, 3, 4, 1]
b = [3, 4, 1, 2, 1, 3, 4, 1]

def lcs(s_1, s_2):
	if len(s_1) == 1 or len(s_2) == 1:
		if s_1[-1] == s_2[-1]:
			return 1
		else:
			return 0
	else:
		if s_1[-1] == s_2[-1]:
			return 1 + lcs(s_1[:-1], s_2[:-1])
		else:
			return max(lcs(s_1[:-1], s_2), lcs(s_1, s_2[:-1]))

print lcs(a, b)