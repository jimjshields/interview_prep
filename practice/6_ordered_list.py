# Implement an ordered list ADT
# Ordered List: a linked list with unique values of a comparable type in which they are sorted based on that comparison.
# Associated methods:
# add(data), remove(data), is_empty(), pop(index), search(data), size(), index(data)
# forgot index
# Also need a Node class

class Node(object):
	"""Represents a node in an ordered list."""

	def __init__(self, data):
		"""A node with some data payload."""

		self.data = data
		self.next = None

	def get_data(self):
		"""Getter for the node's data."""

		return self.data

	def set_data(self, new_data):
		"""Setter for the node's data."""

		self.data = new_data

	def get_next(self):
		"""Gets the next node."""

		return self.next

	def set_next(self, next):
		"""Sets the reference to the next node."""

		self.next = next

class OrderedList(object):
	"""Represents an ordered list ADT."""

	def __init__(self):
		"""Empty ordered list."""

		self.head = None

	def is_empty(self):
		"""Checks if it's empty."""

		return self.head == None

	def add(self, data):
		"""Adds a node in the right spot."""

		node = Node(data)
		if self.is_empty():
			self.head = node
		else:
			current = self.head
			previous = None
			while current != None and current.get_data() < data:
				previous = current
				current = current.get_next()
			if current == None:
				previous.set_next(node)
			elif previous == None:
				node.set_next(current)
				self.head = node
			else:
				node.set_next(current)
				previous.set_next(node)

	def remove(self, data):
		"""Removes a node with the given data."""

		if self.is_empty():
			return False
		else:
			current = self.head
			previous = None
			while current != None and current.get_data() != data:
				previous = current
				current = current.get_next()
			if current == None:
				return False
			else:
				if previous == None:
					self.head = current.get_next()
				elif current.get_next() == None:
					previous.set_next(None)
				else:
					previous.set_next(current.get_next())

	def size(self):
		"""Returns the size of the ordered list."""

		if self.is_empty():
			return 0
		else:
			current = self.head
			count = 0
			while current != None:
				count += 1
				current	= current.get_next()	

		return count

	def pop(self, index):
		"""Removes and returns a node at a given index."""

		if self.is_empty():
			return False
		else:
			count = 0
			current = self.head
			previous = None
			while current != None and count < index:
				previous = current
				current = current.get_next()
				count += 1

			if current == None:
				return False
			else:
				if previous == None:
					self.head = current.get_next()
					return current.get_data()
				elif current.get_next() == None:
					previous.set_next(None)
					return current.get_data()
				else:
					previous.set_next(current.get_next())
					return current.get_data()

	def search(self, data):
		"""Searches the list for a given datapoint."""

		found = False
		if self.is_empty():
			return found
		else:
			current = self.head
			previous = None
			while current != None and not found and current.get_data() < data:
				previous = current
				current = current.get_next()
			if current.get_data() == data:
				found = True
		return found

	def index(self, data):
		"""Returns the index of a given datapoint."""

		if not self.search(data):
			return False
		else:
			current = self.head
			previous = None
			index = 0
			while current.get_data() != data:
				previous = current
				current = current.get_next()
				index += 1
			return index


a = OrderedList()
a.add(1)
a.add(-1)
a.add(5)
a.add(10)
a.add(100)
a.add(-100)
a.pop(3)
print a.search(10)
print a.index(-100)
current = a.head
while current != None:
	print current.get_data()
	current = current.get_next()