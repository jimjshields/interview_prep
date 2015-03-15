# Implement a min binary heap ADT.
# Properties: a list of ints representing a complete binary tree.
# Each parent is less than or equal to both children.
# Insertion and deletion should take O(log(n)) time.
# Insertion: need to percolate the new key up to where it should be.
# Deletion: need to replace the root (the min value) w/ the new min.

class BinaryHeap(object):
	"""Represents a binary heap ADT. Has methods for insertion, deletion,
	   percolating up and down."""

	def __init__(self):

		# 0 at the start - allows for integer division to find parents.
		self.heap = [0]

		# Use size for other methods.
		self.current_size = 0

	def insert(self, key):
		"""Inserts a key into the tree and percs it up to where it should be."""

		# Put it at the end of the heap.
		self.heap.append(key)
		self.current_size += 1

		# Percolate it up to where it needs to be.
		self.perc_up(key, current_size)

	def perc_up(self, key, size):
		"""Percolate the given key up to where it should be."""

		current_index = size
		while key < self.heap[current_index // 2]:
			child = key
			parent = self.heap[current_index // 2]

			# Switch parent and child.
			self.heap[current_index], self.heap[current_index // 2] = parent, child
			current_index //= 2

	def del_min(self):
		"""Deletes and returns the min key and reorders the binary heap."""

		min_key = self.heap[1]

		# For clarity's sake.
		self.heap[1] = None
		

