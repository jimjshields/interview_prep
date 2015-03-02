# Implement a binary tree ADT
# Tree: consists of a root node and 0 or more subtrees, each of which is a tree
# Characteristics: each node (except root) has a single parent
# Each node is unique/has a unique path
# Binary tree: no more than 2 children to each parent

class BinaryTree(object):
	"""Represents a tree ADT."""

	def __init__(self, root_node):
		"""Initializes a tree with a root."""

		self.root = root_node
		self.left_child = None
		self.right_child = None

	def insert_left(self, new_node):
		"""Adds a left child to any given level of the binary tree."""

		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			temp = BinaryTree(new_node)
			temp.left_child = self.left_child
			self.left_child = temp

	def insert_right(self, new_node):
		"""Adds a right child to any given level of the binary tree."""

		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			temp = BinaryTree(new_node)
			temp.right_child = self.right_child
			self.right_child = temp

	def get_left_child(self):
		return self.left_child

	def get_right_child(self):
		return self.right_child

	def set_root_val(self, new_root_obj):
		self.root = new_root_obj

	def get_root_val(self):
		return self.root