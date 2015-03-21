# from collections import Stack

# # Requirements:
# # {1..3} -> 1 2 3
# # {1, 2} -> 1 2
# # {a..c} -> a b c
# # {hello, world} -> hello word
# # a{1..3}b -> a1b a2b a3b

# def brace_expansion(brace_string):
# 	"""Expands a given brace_string to a bash-style expansion."""

# 	brace_stack = Stack()
# 	string_ind = 0
# 	while string_ind < len(brace_string):
# 		if 
# 		if brace_string[string_ind] == '{':
# 			brace_stack.push(brace_string[string_ind])

def FindMatchedBraces(text, position = -1): 
	"Search for nested start and end brace in text starting from position" 
	braceDepth = 0 
	nextClose = -1 
	first = True 

	# Search for a { 
	# is it closer than the nearest } ? 
	# Yes : increase brace depth 
	# No : decrease brace depth 
	# When we reach braceDepth == 0, we have found our close brace 
	while braceDepth or first: 

		nextOpen = text.find("{", position+1) 
		nextClose = text.find("}", position+1) 

		if first and nextOpen >= 0: 
			startBrace = nextOpen 
			first = False 

		if nextOpen < nextClose and nextOpen >= 0: 
			braceDepth += 1 
			position = nextOpen 
		elif nextClose >= 0: 
			braceDepth -= 1 
			position = nextClose 
		else: 
			raise NoBraces() 

	return startBrace, position 

try: start, end = FindMatchedBraces(text) 
except NoBraces: 
	# There are no braces! Nothing to expand! 
	return [text]

# Split the text into three bits, '{pre,,post}amble'. The 'pre' is anything 
# before expansion, the '' is the bit that needs expanding and gluing to 
# the pre and the post. After gluing together, we can recursively expand 
# again 
preamble = text[:start] 
amble = text[start+1:end] 
postamble = text[end+1:] 