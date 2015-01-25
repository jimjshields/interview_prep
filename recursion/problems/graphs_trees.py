class Node(object):
	def __init__(self, value, l=None, r=None):
		self.value = value
		self.left = l
		self.right = r

tree1 = Node(1, 
			Node(2,
				Node(3),
				Node(4)),
			Node(5,
				Node(6),
				Node(7)))

tree2 = Node(1,
			Node(2, 
				Node(3)),
			Node(4, 
				Node(5,
					Node(6),
					Node(7))))

tree3 = Node(1, Node(2, Node(3), Node(4)))

def treeSum(tree):
	# if you get to a bottom node
	if tree.left is None and tree.right is None:
		# return the value of that node
		return tree.value
	# if you get to a node with just a right
	elif tree.left is None:
		# return the recursive sum of the right side
		return tree.value + treeSum(tree.right)
	# if you get to a node with just a left	
	elif tree.right is None:
		# return the recursive sum of the left side
		return tree.value + treeSum(tree.left)
	# if it has both
	else:
		# return the recursive sum of both
		return tree.value + treeSum(tree.left) + treeSum(tree.right)

print treeSum(tree2)

def printTree(tree, treeList=[]):
	print treeList
	if tree.left is None and tree.right is None:
		treeList.append(tree.value)
	elif tree.left is None:
		treeList.append(tree.value)
		printTree(tree.right, treeList)
	elif tree.right is None:
		treeList.append(tree.value)
		printTree(tree.left, treeList)
	else:
		treeList.append(tree.value)
		printTree(tree.left)
		printTree(tree.right)

printTree(tree2)
