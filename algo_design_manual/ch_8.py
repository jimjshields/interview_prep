# String compare algorithm.

def match(c, d):
	if c == d:
		return 0
	else:
		return 1

def indel(c):
	return 1

def string_compare(s, t, i, j):
	k = 0
	lowest_cost = len(s) + len(t)

	if i == 0:
		return j * indel(' ')
	if j == 0:
		return i * indel(' ')

	opt = {
		'MATCH': string_compare(s, t, i - 1, j - 1) + match(s[i], t[j]),
		'INSERT': string_compare(s, t, i, j - 1) + indel(t[j]),
		'DEL': string_compare(s, t, i - 1, j) + indel(s[i])
	}

	lowest_cost = opt['MATCH']
	for k in ['INSERT', 'DEL']:
		if opt[k] < lowest_cost:
			lowest_cost = opt[k]

	return lowest_cost

print string_compare(' edit', ' edit', 4, 5)
