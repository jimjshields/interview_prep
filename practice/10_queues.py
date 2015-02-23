# Queue ADT
# Methods: enqueue, dequeue, is_empty, size
# FIFO

class Queue(object):
	"""A queue ADT."""

	def __init__(self):
		"""Initializes an empty queue."""

		self.items = []

	def enqueue(self, item):
		"""Adds an item to the queue."""

		self.items.append(item)

	def dequeue(self):
		"""Removes and returns the first item in the queue."""

		return self.items.pop(0)

	def is_empty(self):
		"""Returns boolean for an empty queue."""

		return self.items == []

	def size(self):
		"""Returns the size of the queue."""

		return len(self.items)