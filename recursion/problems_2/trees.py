import unittest

class TestBinTreeSum(unittest.TestCase):

    def setUp(self):
        self.input = tree1
        self.output = 28
        self.input_2 = tree2
        self.output_2 = 10

    def test_bin_tree_sum(self):
        self.assertEqual(bin_tree_sum(self.input), self.output)
        self.assertEqual(bin_tree_sum(self.input_2), self.output_2)

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
             Node(4))

def bin_tree_sum(tree, total=0):
    """Returns the sum of a binary tree."""

    if not (tree.left or tree.right):
        return tree.value
    else:
        if tree.left and tree.right:
            return tree.value + bin_tree_sum(tree.left) + bin_tree_sum(tree.right)
        elif tree.left:
            return tree.value + bin_tree_sum(tree.left)
        else:
            return tree.value + bin_tree_sum(tree.right)


if __name__ == '__main__':
    unittest.main()