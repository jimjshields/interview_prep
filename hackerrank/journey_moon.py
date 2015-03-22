# https://www.hackerrank.com/challenges/journey-to-the-moon

# Conncted components - store the astronauts in graphs and determine how many different components there are
# Once you have that, compute the diff combos by taking the number in each component, multiplying by all of the other ones, and adding it to the same

class Graph(object):
	"""Represents an undirected graph as a list of sets."""

	def __init__(self):
		"""Initializes with an empty graph."""

		self.nodes = []

	def add_pair(self, a, b):
		"""Takes a graph and a pair of numbers and adds the numbers to the graph.
		   Accounts for the numbers already being there."""

		found = False
		for num_set in self.nodes:
			if a in num_set or b in num_set:
				num_set.add(a)
				num_set.add(b)
				found = True
		if not found:
			self.nodes.append(set([a, b]))

	def get_num_valid_combos(self):
		"""Given a graph of connected components, returns the number of valid
		   two-item combos, where two items in the same set can't be combined."""

		total = 0
		graph_size = reduce(lambda x, num_set: x + len(num_set), self.nodes, 0)
		
		for num_set in self.nodes:
			total += len(num_set) * (graph_size - len(num_set))
			graph_size -= len(num_set)

		return total

	def __str__(self):
		return '%s' % (self.nodes)

graph = Graph()
graph.add_pair(0, 1)
graph.add_pair(0, 4)
graph.add_pair(0, 10)
graph.add_pair(1, 3)
graph.add_pair(12, 2443)
graph.add_pair(13132, 12312)
graph.add_pair(32323, 43234)
graph.add_pair(1313, 1231)
graph.add_pair(13, 123)
graph.add_pair(13132, 123)
graph.add_pair(13132, 1)
graph.add_pair(1, 12312)

print graph