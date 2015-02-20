# implement an unordered linked list
# linked list: an object with a pointer to the first item in the list,
# each successive item holds a pointer to the next item and some payload/data
# the last item points to None
# methods: add, remove, size, isEmpty, search
# two classes - Node and UnorderedLinkedList

### Issues - forgot certain functionality (search, append, pop, index, insert; get_data, set_data)
### 	   - often forget 'self' as an argument
### 	   - traversing the list gets confusing - make sure I account for empty list and always have current/previous nodes

class Node(object):
	"""Represents a node in a linked list. Has data and a pointer to the next node."""

	def __init__(self, data, next=None):
		"""Initializes a node."""

		self.data = data
		self.next = next

	def get_next(self):
		"""Returns the next node in the linked list."""

		return self.next

	def set_next(self, node):
		"""Sets the next node in the linked list."""

		self.next = node

	def get_data(self):
		"""Returns the data of the given node."""

		return self.data

	def set_data(self, new_data):
		"""Sets the data of the given node."""

		self.data = new_data

class UnorderedLinkedList(object):
	"""Represents an unordered linked list ADT. Assumes all data is unique."""

	def __init__(self):
		"""Initializes an empty linked list."""

		self.head = None

	def add(self, data):
		"""Adds a node to the end of the list."""

		current = self.head
		previous = None
		node = Node(data)

		while current != None:
			previous = current
			current = current.get_next()

		if previous != None:
			previous.set_next(node)
		else:
			self.head = node

	def remove(self):
		"""Removes the node at the end of the list."""

		current = self.head
		previous = None

		while current != None:
			previous = current
			current = current.get_next()

		if previous != None:
			previous.set_next(None)
		else:
			self.head = None

	def size(self):
		"""Returns the size of the linked list."""

		current = self.head
		size = 0

		while current != None:
			size += 1
			current = current.get_next()

		return size

	def is_empty(self):
		"""Returns bool for whether the list is empty."""

		return self.head == None

	def search(self, data):
		"""Returns bool for whether the given data is in the list."""

		current = self.head
		previous = None

		while current != None and current.get_data() != data:
			previous = current
			current = current.get_next()

		if current == None:
			return False
		else:
			return True

	def pop(self, index=None):
		"""Removes and returns the item at the given index in the list.
		   Default is None; if None, pop the last item."""

		current = self.head
		previous = None

		if index == None:
			while current.get_next() != None:
				previous = current
				current = current.get_next()

			previous.set_next(None)
			return current.get_data()
		else:
			count = 0
			while current.get_next() != None and count < index:
				previous = current
				current = current.get_next()
				count += 1

			previous.set_next(current.get_next())
			return current.get_data()

	def index(self, data):
		"""Returns the index number of the given data."""

		count = 0
		current = self.head

		while current != None and current.get_data() != data:
			current = current.get_next()
			count += 1

		if current.get_data() == data:
			return count
		else:
			return False

	def print_data(self):
		"""Prints every item in the list."""

		current = self.head

		while current != None:
			print current.get_data()
			current = current.get_next()


### Manual testing

new_list = UnorderedLinkedList()
print "{} should be True.".format(new_list.is_empty())
new_list.add(1)
print "{} should be False.".format(new_list.is_empty())
print "{} should be 1.".format(new_list.size())
new_list.add(10)
new_list.add(14)
new_list.add(15)
new_list.add(20)
print "{} should be 5.".format(new_list.size())
print "{} should be True.".format(new_list.search(10))
print "{} should be False.".format(new_list.search(5))
print new_list.pop()
new_list.pop(2)
new_list.print_data()
print new_list.index(10)