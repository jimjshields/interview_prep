# Stack ADT
# Necessary methods: add, remove, is_empty, size, search (?)
# Concepts: LIFO, list implementation, high-speed in Python
# Forgot - peek

class Stack(object):
	"""A stack ADT."""

	def __init__(self):
		"""Initializes empty stack ADT."""

		self.items = []

	def add(self, item):
		"""Adds an item to the top of the stack."""

		self.items.append(item)

	def remove(self):
		"""Removes and returns the item at the top of the stack."""

		return self.items.pop()

	def is_empty(self):
		"""Returns boolean for empty stack."""

		return self.items == []

	def size(self):
		"""Returns size of stack."""

		return len(self.items)

	def peek(self):
		"""Returns item on the top of the stack."""

		return self.items[-1]