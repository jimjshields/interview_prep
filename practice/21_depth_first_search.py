class Vertex(object):
	"""A vertex in a graph."""

	def __init__(self, key):
		"""Initializes a vertex with a given data payload."""

		self.id = key
		self.connections = {}
		self.color = 'white'

	def add_connection(self, other, weight=None):
		"""Adds a connected vertex with a given weight."""

		self.connections[other] = weight

	def get_connections(self):
		"""Returns the list of connected vertices."""

		return self.connections.keys()

	def get_id(self):
		"""Returns the id of the vertex."""

		return self.id

	def get_weight(self, other):
		return self.connections[other]

	def set_color(self, color):
		"""Setter for color."""

		self.color = color

	def get_color(self):
		"""Returns a vertex's color."""

		return self.color

	def set_dist(self, dist):
		"""Setter for distance."""

		self.dist = dist

	def get_dist(self):
		"""Returns a vertex's distance."""

		return self.dist

	def set_pred(self, pred):
		"""Setter for predecessor."""

		self.pred = pred

	def get_pred(self):
		"""Returns a vertex's predecessor."""

		return self.pred

	def __str__(self):
		"""String representation of a vertex."""

		return "V{} connected to {}".format(self.id, [x.id for x in self.connections])

class Graph(object):
	"""A graph ADT."""

	def __init__(self):
		"""Initializes an empty graph."""

		self.vertices = {}
		self.num_vertices = 0

	def add_vertex(self, key):
		"""Adds a vertex to the graph."""

		self.num_vertices += 1
		new_vertex = Vertex(key)
		self.vertices[key] = new_vertex
		return new_vertex

	def add_edge(self, from_vertex, to_vertex, weight=None):
		"""Adds an edge between two given vertices."""

		if from_vertex not in self:
			self.add_vertex(from_vertex)
		elif to_vertex not in self:
			self.add_vertex(to_vertex)
		self.vertices[from_vertex].add_connection(self.vertices[to_vertex], weight)

	def get_vertex(self, vert_key):
		"""Returns a vertex associated w/ a vertex key."""

		if vert_key in self.vertices:
			return self.vertices[vert_key]
		else:
			return None

	def get_vertices(self):
		"""Returns a list of all vertices in the graph."""

		return self.vertices.keys()

	def __contains__(self, vert_key):
		"""Overrides the 'in' operator. Returns True if given vertex is in graph."""

		return vert_key in self.vertices.keys()

class Stack(object):
	"""A stack ADT."""

	def __init__(self):
		"""Initializes empty stack ADT."""

		self.items = []

	def add(self, item):
		"""Adds an item to the top of the stack."""

		self.items.append(item)

	def remove(self):
		"""Removes and returns the item at the top of the stack."""

		return self.items.pop()

	def is_empty(self):
		"""Returns boolean for empty stack."""

		return self.items == []

	def size(self):
		"""Returns size of stack."""

		return len(self.items)

	def peek(self):
		"""Returns item on the top of the stack."""

		return self.items[-1]

# Implement depth-first search
# http://en.wikipedia.org/wiki/Depth-first_search
# Essentially explore every node by starting w/ one and following as far as possible, then backtracking

def dfs(graph, start_vertex):
	"""Searches a graph depth-first."""

	node_stack = Stack()
	start_vertex.set_dist(0)
	node_stack.add(start_vertex)
	
	while node_stack.size() > 0:
		current = node_stack.remove()
		if current.get_color() == 'white':
			current.set_color('gray')
			for nbr in current.get_connections():
				if nbr.get_color() == 'white':
					nbr.set_dist(current.get_dist() + 1)
					nbr.set_pred(current)
					node_stack.add(nbr)
			current.set_color('black')
			print current.get_id()

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_edge(1, 20)
g.add_edge(20, 2100)
g.add_edge(2100, 100)
g.add_edge(1, 5)
g.add_edge(5, 100)
g.add_edge(100, 20)
g.add_edge(1, 10)

dfs(g, g.vertices[1])


