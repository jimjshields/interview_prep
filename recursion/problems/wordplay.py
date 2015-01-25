# generate all reorderings/permutations of a set of letters

def permutations(elements):
	"""Input: list or string
	   Output: List of lists of all possible permutations of those elements"""
	# convert to list if a string
	if type(elements) is str:
		elements = list(elements)
	# print "Calling perm on %s" % (elements)
	res = []
	if len(elements) == 1:
		 res = [elements]
	else:
		for i, item in enumerate(elements):
			# print "Item: %s" % (item)
			for perm in permutations(elements[:i] + elements[i + 1:]):
				# print "Perm: %s" % (perm)
				# print "Adding %s to res" % ([item] + perm)
				res += [[item] + perm]
	return res

def wordCombos(letters, length):
	"""Input: String of letters; length of desired combinations
	   Output: List of all combinations of letters of given length"""
	
	res = []
	for i in range(len(letters)):
		# base case - 1 letter
		if length == 1:
			res.append(letters[i])
		# otherwise, recursively call this on a smaller input
		else:
			for c in wordCombos(letters[i + 1:], length - 1):
				# once you get the smaller combos, add those to the original letter
				res.append(letters[i] + c)
	return res

def allWordCombos(letters):
	"""Input: String of letters
	   Output: List of all possible combinations of those letters"""

	for i in range(1, len(letters) + 1):
		for word in wordCombos(letters, i):
			yield word

def allPermutations(letters):
	"""Input: String of letters
	   Output: List of all possible permutations 
	   of those letters of any size"""

	for combo in allWordCombos(letters):
		comboPerms = [''.join(perm) for perm in permutations(combo)]
		for comboPerm in comboPerms:
			yield comboPerm

f = open('sowpods.txt', 'r')
sowpodsWords = [word.rstrip().lower() for word in f]

def findScrabbleWords(letters, wordList):
	legalWords = []
	for word in allPermutations(letters):
		if word in wordList and word not in legalWords:
			legalWords.append(word)
	return legalWords

print findScrabbleWords('testin', sowpodsWords)