# AVL Tree
# Self-balancing binary tree
# Heights of the two subtrees of any node differ by at most one
# If they differ by more than one automatic rebalancing will happen
# Lookup, insertion, deletion all take O(log(n)) time in avg. and worst cases
# Same operations as a binary search tree, but with rebalancing after any modifications

# Implementing a regular tree as a class

class BinaryTree(object):
	"""Binary Tree ADT."""

	def __init__(self, root_obj):
		self.key = root_obj
		self.left_child = None
		self.right_child = None

	def insert_left(self, new_node):
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	def insert_right(self, new_node):
		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.right_child = self.right_child
			self.right_child = t

	def get_left_child(self):
		return self.left_child

	def get_right_child(self):
		return self.right_child

	def set_root_val(self, obj):
		self.key = obj

	def get_root_val(self, obj):
		return self.key

# Implementing Binary Search Tree

class BinarySearchTree(object):
	"""Binary Search Tree ADT."""

	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

class TreeNode(object):
	"""A node in a BinarySearchTree."""

	def __init__(self, key, value, left=None, right=None, parent=None):
		self.key = key
		self.payload = value
		self.left_child = left
		self.right_child = right
		self.parent = parent

	def has_left_child(self):
		return self.left_child

	def has_right_child(self):
		return self.right_child

	def is_left_child(self):
		return self.parent and self.parent.left_child == self

	def is_right_child(self):
		return self.parent and self.parent.right_child == self

	def is_root(self):
		return not self.parent

	def is_leaf(self):
		return not(self.right_child or self.left_child)

	def has_any_children(self):
		return self.left_child or self.right_child

	def has_both_children(self):
		return self.left_child and self.right_child

	def replace_node_data(self, key, value, lc, rc):
		self.key = key
		self.payload = value
		self.left_child = lc
		self.right_child = rc
		if self.has_left_child():
			self.left_child.parent = self
		if self.has_right_child():
			self.right_child.parent = self


# Implementing an AVL tree as a class

class AVLTree(object):
	"""AVL Tree ADT."""