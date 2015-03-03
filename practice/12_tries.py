# Implement a Trie

# http://en.wikipedia.org/wiki/Trie
# 1. What is a trie?
# It's a ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings
# Unlike binary search tree - no node stores the key associated w/ the node
# Instead, its position in the tree defines the key w/ which it's associated
# root - the empty string
# most common w/ character strings, but that's not a requirement

# 2. Why? / Applications
# Advantages over binary search tree
# Can also replace a hash table
# Worst case - lookup is faster than an imperfect hash table (O(m) vs. O(n) - where m is the length of the string - O(n) is worst case in hash table w/ collisions)
# No collisions of diff keys in a trie
# Buckets only necessary if a single key stores more than one value
# Tries can be slower than hash tables in some cases - esp. if data directly accessed on hard disk

# Needs a Node class and a Trie class
# Unfinished for the moment

# import unittest

# class Node(object):
# 	"""A node to be filled in by trie methods."""

# 	def __init__(self, key, children):
# 		"""A node with a key and empty list of children."""

# 		self.key = key
# 		self.children = {}

# 	def add_child(self, key):
# 		"""Add a child with a given key to the node."""

# 		self.children[key] = 

# class Trie(object):
# 	"""A Trie to be filled in by nodes."""

# 	def __init__(self):
# 		"""An empty trie."""

# 		self.root = Node(None)

# 	def add_word(self, word):
# 		"""Add a word to the trie."""

# 		start = word[0]
# 		if start in self.root.children:
# 			start = self.root.children[start]
# 			self.add_word(start, word[1:])
# 		else:
# 			self.root.children[start].add_word(start, word[1:])


# https://reterwebber.wordpress.com/2014/01/22/data-structure-in-python-trie/
# http://www.geeksforgeeks.org/trie-delete/

def make_trie(*args):
	"""Make a trie by given words."""

	trie = {}

	for word in args:
		if type(word) != str:
			raise TypeError('Trie only works with strings!')
		temp_trie = trie
		for letter in word:
			temp_trie = temp_trie.setdefault(letter, {})
		temp_trie = temp_trie.setdefault('_end_', '_end_')

	return trie