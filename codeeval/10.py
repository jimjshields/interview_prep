def forceWidth(num, width):
	num = str(num).strip()
	if len(num) > width:
		return "%s is too long for width %s" % (num, width)
	elif len(num) <= width:
		num = num + ' ' * (width - len(num))
	return num

def multTable(num, width):
	"""Input: integer
	   Output: prints multiplication table (str) of size num
	   		   width determines amount of total space for each num"""
	table = []
	for i in range(1, num + 1):
		line = [n * i for n in range(1, num + 1)]
		table.append(line)

	for line in table:
		for i, n in enumerate(line):
			if i == len(line) - 1:
				print n,
			else:
				print forceWidth(n, width),
		print "\n",

multTable(12, 4)