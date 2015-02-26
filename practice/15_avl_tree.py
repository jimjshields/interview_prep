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

	def put(self, key, value):
		"""Inserts a node with key and value on the tree."""

		if self.root:
			self._put(key, value, self.root)
		else:
			self.root = TreeNode(key, value)
		self.size += 1

	def _put(self, key, value, current_node):
		"""Private method for recursively inserting a node at the right place."""

		if key < current_node.key:
			if current_node.has_left_child():
				self._put(key, value, current_node.left_child)
			else:
				current_node.left_child = TreeNode(key, value, parent=current_node)
		else:
			if current_node.has_right_child():
				self._put(key, value, current_node.right_child)
			else:
				current_node.right_child = TreeNode(key, value, parent=current_node)

	def __setitem__(self, key, value):
		"""Overloads the [] operator for Binary Trees."""

		self.put(key, value)

	def get(self, key):
		if self.root:
			res = self._get(key, self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	def _get(self, key, current_node):
		"""Returns the node specified by the given key or None."""

		if not current_node:
			return None
		elif current_node.key == key:
			return current_node
		elif key < current_node.key:
			return self._get(key, current_node.left_child)
		else:
			self._get(key, current_node.right_child)

	def __getitem__(self, key):
		"""Overloads the accessor operator."""

		return self.get(key)

	def __contains__(self, key):
		"""Overloads the 'in' operator."""

		if self._get(key, self.root):
			return True
		else:
			return False

	def delete(self, key):
		"""Deletes a node."""

		if self.size > 1:
			node_to_remove = self._get(key, self.root)
			if node_to_remove:
				self.remove(node_to_remove)
				self.size -= 1
			else:
				raise KeyError('Error, key not in tree.')
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size -= 1
		else:
			raise KeyError('Error, key not in tree.')

	def __delitem__(self, key):
		"""Overloads the 'del' operator."""

		self.delete(key)

	def remove(self, current_node):
		"""Removes the node from the tree and updates all related nodes."""

		# No children
		if current_node.is_leaf():
			if current_node == current_node.parent.left_child:
				current_node.parent.left_child = None
			else:
				current_node.parent.right_child = None
		elif current_node.has_both_children():
			succ = current_node.find_successor()
			succ.splice_out()
			current_node.key = succ.key
			current_node.payload = succ.payload

		# One child
		else:
			if current_node.has_left_child():
				if current_node.is_left_child():
					current_node.left_child.parent = current_node.parent
					current_node.parent.left_child = current_node.left_child
				elif current_node.is_right_child():
					current_node.right_child.parent = current_node.parent
					current_node.parent.right_child = current_node.right_child
				else:
					current_node.replace_node_data(current_node.left_child.key,
												   current_node.left_child.payload,
												   current_node.left_child.left_child,
												   current_node.left_child.right_child)
			else:
				if current_node.is_left_child():
					current_node.right_child.parent = current_node.parent
					current_node.parent.left_child = current_node.right_child
				elif current_node.is_right_child():
					current_node.right_child.parent = current_node.parent
					current_node.parent.right_child = current_node.right_child
				else:
					current_node.replace_node_data(current_node.right_child.key,
												   current_node.right_child.payload,
												   current_node.right_child.left_child,
												   current_node.right_child.right_child)


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

	def find_successor(self):
		"""Returns the successor node, if there is one, for proper removal."""

		succ = None
		if self.has_right_child():
			succ = self.right_child.find_min()
		else:
			if self.parent:
				if self.is_left_child():
					succ = self.parent
				else:
					self.parent.right_child = None
					succ = self.parent.find_successor()
					self.parent.right_child = self
		return succ

	def find_min(self):
		"""Finds the minimum node from the given node."""

		current = self
		while current.has_left_child():
			current = current.left_child
		return current

	def splice_out(self):
		if self.is_leaf():
			if self.is_left_child():
				self.parent.left_child = None
			else:
				self.parent.right_child = None
		elif self.has_any_children():
			if self.has_left_child():
				if self.is_left_child():
					self.parent.left_child = self.left_child
				else:
					self.parent.right_child = self.right_child
				self.left_child.parent = self.parent
			else:
				if self.is_left_child():
					self.parent.left_child = self.right_child
				else:
					self.parent.right_child = self.right_child
				self.right_child.parent = self.parent

	def __iter__(self):
		"""Overloads the iteration operator w/ an inorder traversal."""

		if self:
			if self.has_left_child():
				for elem in self.left_child:
					yield elem
			yield self.key
			if self.has_right_child():
				for elem in self.right_child:
					yield elem

# Implementing an AVL tree as a class

class AVLTree(BinarySearchTree):
	"""AVL Tree ADT. Has methods for self-balancing."""

	def _put(self, key, value, current_node):
		"""Overrides default BST _put method to include calling of
		   update_balance."""

		if key < current_node.key:
			if current_node.has_left_child():
				self._put(key, value, current_node.left_child)
			else:
				current_node.left_child = TreeNode(key, value, parent=current_node)
				self.update_balance(current_node,left_child)
		else:
			if current_node.has_right_child():
				self._put(key, value, current_node.right_child)
			else:
				current_node.right_child = TreeNode(key, value, parent=current_node)
				self.update_balance(current_node.right_child)

	def update_balance(self, node):
		"""Determines if the node needs rebalancing and recursively calls the 
		   rebalancing method on all parents if so."""

		if node.balance_factor > 1 or node.balance_factor < -1:
			self.rebalance(node)
			return
		if node.parent != None:
			if node.is_left_child():
				node.parent.balance_factor += 1
			elif node.is_left_child():
				node.parent.balance_factor -= 1

			if node.parent.balance_factor != 0:
				self.update_balance(node.parent)

	def rotate_left(self, rot_root):
		"""Rotates the given node."""

		new_root = rot_root.right_child
		rot_root.right_child = new_root.left_child
		if new_root.left_child != None:
			new_root.left_child.parent = rot_root
		new_root.parent = rot_root.parent
		if rot_root.is_root():
			self.root = new_root
		else:
			if rot_root.is_left_child():
				rot_root.parent.left_child = new_root
			else:
				rot_root.parent.right_child = new_root
		new_root.left_child = rot_root
		rot_root.parent = new_root
		rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
		new_root.balance_factor = new_root.balance_factor + 1 + max(new_root.balance_factor, 0)

	def rotate_right(self, rot_root):
		"""Rotates the given node."""

		new_root = rot_root.left_child
		rot_root.left_child = new_root.right_child
		if new_root.right_child != None:
			new_root.right_child.parent = rot_root
		new_root.parent = rot_root.parent
		if rot_root.is_root():
			self.root = new_root
		else:
			if rot_root.is_right_child():
				rot_root.parent.right_child = new_root
			else:
				rot_root.parent.left_child = new_root
		new_root.right_child = rot_root
		rot_root.parent = new_root
		rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
		new_root.balance_factor = new_root.balance_factor + 1 + max(new_root.balance_factor, 0)

	def rebalance(self, node):
		if node.balance_factor < 0:
			if node.right_child.balance_factor > 0:
				self.rotate_right(node.right_child)
				self.rotate_left(node)
			else:
				self.rotate_left(node)
		elif node.balance_factor > 0:
			if node.left_child.balance_factor < 0:
				self.rotate_left(node.left_child)
				self.rotate_right(node)
			else:
				self.rotate_right(node)




