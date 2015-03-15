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
		while current_index // 2 > 0:
			if key < self.heap[current_index // 2]:
				child = key
				parent = self.heap[current_index // 2]

				# Switch parent and child.
				self.heap[current_index], self.heap[current_index // 2] = parent, child
				current_index //= 2

	def del_min(self):
		"""Deletes and returns the min key and reorders the binary heap."""

		min_key = self.heap[1]

		# Get rid of the last key and put it at the root, in order to maintain
		# the binary heap structure property.
		self.heap[1] = self.heap.pop()
		self.current_size -= 1
		root = self.heap[1]

		# Move the root down to where it should be, reordering it correctly.
		self.perc_down(root, self.current_size)

		return min_key

	def perc_down(self, root, size):
		"""Given the root and current heap size, moves the root down to 
		   where it should be."""

		current_index = 1

		# Continue looping while the root is greater than both of its children.
		while root > self.heap[current_index * 2] and root > self.heap[(current_index * 2) + 1]:

			# Check for which of the children is smaller, that should be the new parent.
			if self.heap[current_index * 2] > self.heap[(current_index * 2) + 1]:
				min_child_index = (current_index * 2) + 1
			else:
				min_child_index = (current_index * 2)
			min_child = self.heap[min_child_index]

			# Switch the root and the min child of the root.
			self.heap[current_index], self.heap[min_child_index] = min_child, root

