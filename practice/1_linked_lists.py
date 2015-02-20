# implement an unordered linked list
# linked list: an object with a pointer to the first item in the list,
# each successive item holds a pointer to the next item and some payload/data
# the last item points to None
# methods: add, remove, size, isEmpty, ???

class LinkedList(object):
	"""Represents an unordered linked list ADT."""

	def __init__(self):
		"""Initializes an empty linked list."""

		self.head = None

	def add(self, item):
		"""Adds an item to the end of the list."""

		