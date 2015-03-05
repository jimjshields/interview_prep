class BinaryTree(object):
 
	def __init__(self, root):
		self.root = root
		self.root.depth = 0
 
class Node(object):
 
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.depth = None
		self.parent = None
 
	def set_left(self, left):
		self.left = left
		self.left.parent = self
		self.left.depth = self.depth + 1
 
	def set_right(self, right):
		self.right = right
		self.right.parent = self
		self.right.depth = self.depth + 1
 
	def is_leaf(self):
		return (not self.right and not self.left)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)

t = BinaryTree(n1)

n1.set_right(n2)
n1.set_left(n3)
n2.set_left(n4)
n3.set_right(n5)

t2 = BinaryTree(n6)

n6.set_right(n7)
n7.set_right(n8)
n6.set_left(n9)
n8.set_right(n10)

def is_bst(node, nodes=[]):
	current = node
	if current:
		is_bst(current.left)
		nodes.append(current)
		is_bst(current.right)
	print [node.val for node in nodes]		

is_bst(n6)