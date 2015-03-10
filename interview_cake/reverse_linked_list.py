# Reverse a linked list.

class LinkedList(object):
	"""Represents a linked list ADT."""

	def __init__(self):
		self.head = None

	def set_head(self, head):
		self.head = head

	def get_head(self):
		return self.head

	def traverse(self):
		current = self.get_head()
		while current != None:
			print current.data
			current = current.get_next()

class Node(object):
	"""Represents a node in a linked list."""

	def __init__(self, data):
		self.data = data
		self.next = None

	def set_next(self, next):
		self.next = next

	def get_next(self):
		return self.next

def reverse_linked_list(linked_list):
	"""Reverses and returns a linked list object using a stack."""

	node_stack = []

	if not linked_list.get_head():
		return None
	else:
		current = linked_list.get_head()

		# Remove all nodes starting with the head.
		linked_list.set_head(None)
		previous = None
		while current.get_next() != None:
			node_stack.append(current)
			previous = current
			current = current.get_next()

			# Remove the reference from the previous node.
			previous.set_next(None)

	linked_list.set_head(node_stack.pop())
	current = linked_list.get_head()

	while len(node_stack) > 0:
		current.set_next(node_stack.pop())
		current = current.get_next()

	return linked_list

def reverse_linked_list_2(linked_list):
	"""Reverses and returns a linked list object using a stack."""

	# Doesn't work - look into.

	current = linked_list.get_head()
	previous = None
	tail = linked_list.get_head()
	tail_next = None

	while tail.get_next() != None:
		tail = tail.get_next()

	while tail != current:
		tail_next = current
		current = current.get_next()
		tail_next.set_next(tail.get_next())
		tail.set_next(tail_next)
		linked_list.set_head(current)

	return linked_list

ll = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# ll.traverse()

ll.set_head(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)

ll.traverse()

reverse_linked_list(ll).traverse()
reverse_linked_list_2(ll).traverse()