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
		self.perc_up(key, self.current_size)

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

		if self.current_size == 0:
			return None
		else:
			min_key = self.heap[1]

			# Get rid of the last key and put it at the root, in order to maintain
			# the binary heap structure property.
			self.heap[1] = self.heap[self.current_size]
			print 'Min: {0}, new root: {1}'.format(min_key, self.heap[1])
			self.current_size -= 1
			self.heap.pop()

			# Move the root down to where it should be, reordering it correctly.
			self.perc_down(1)

			return min_key

	def perc_down(self, i):
		"""Given the root index, moves the root down to 
		   where it should be."""

		while i * 2 <= self.current_size:
			mc = self.min_child(i)

			# Check for which of the children is smaller, that should be the new parent.
			if self.heap[i] > self.heap[mc]:
				tmp = self.heap[i]
				self.heap[i] = self.heap[mc]
				self.heap[mc] = tmp
			i = mc

	def min_child(self, i):
		"""Returns the index of the minimum child of a given parent index."""

		if i * 2 + 1 > self.current_size:
			return i * 2
		else:
			if self.heap[i * 2] < self.heap[(i * 2) + 1]:
				return i * 2
			else:
				return (i * 2) + 1

	def build_heap(self, a_list):
		"""Given a list, builds a heap."""

		i = len(a_list) // 2
		self.current_size = len(a_list)
		self.heap = [0] + a_list[:]
		while i > 0:
			self.perc_down(i)
			i -= 1


bin_heap = BinaryHeap()
bin_heap.build_heap([9, 6, 5, 2, 3])

print bin_heap.del_min()
print bin_heap.del_min()
print bin_heap.del_min()
print bin_heap.del_min()
print bin_heap.del_min()