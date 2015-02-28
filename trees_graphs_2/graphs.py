# Graph: Collection of vertices and edges
# Directed - one direction

# Representations

class Graph(object):
	"""Represents a directed graph ADT."""

	def __init__(self):
		"""Initializes w/ empty list of vertices."""

		self.vertices = []

	def add_vertex(self, vertex):
		"""Adds a vertex to the graph."""

		self.vertices.append(vertex)

	def get_vertices(self):
		"""Gets the list of vertices from the graph."""

		return self.vertices

	def add_edge(self, vertex_1, vertex_2):
		"""Adds an edge between two given vertices."""

		if vertex_1 not in self.vertices:
			self.add_vertex(vertex_1)
		if vertex_2 not in self.vertices:
			self.add_vertex(vertex_2)

		vertex_1.add_connection(vertex_2)

class UndirectedGraph(Graph):

	def add_edge(self, vertex_1, vertex_2):
		"""Adds an edge in an undirected graph."""

		if vertex_1 not in self.vertices:
			self.add_vertex(vertex_1)
		if vertex_2 not in self.vertices:
			self.add_vertex(vertex_2)

		vertex_1.add_connection(vertex_2)
		vertex_2.add_connection(vertex_1)


class Vertex(object):
	"""Represents a vertex in a graph."""

	def __init__(self, data):
		"""Initializes w/ some data."""

		self.data = data
		self.connections = []
		self.pred = None
		self.dist = 0
		self.color = 'white'

	def add_connection(self, other):
		"""Adds a connection to the given node."""

		self.connections.append(other)

	def get_data(self):
		"""Returns the data of the vertex."""

		return self.data

	def get_connections(self):
		"""Returns a list of all connections of the vertex."""

		return self.connections

	def set_dist(self, dist):
		"""Sets the distance of the vertex from the starting vertex."""

		self.dist = dist

	def get_dist(self):
		"""Returns the distance from the starting vertex."""

		return self.dist

	def set_pred(self, pred):
		"""Sets the predecessor vertex of the current vertex."""

		self.pred = pred

	def get_pred(self):
		"""Returns the predecessor of the current vertex."""

		return self.pred

	def set_color(self, color):
		"""Sets the color of the current vertex."""

		self.color = color

	def get_color(self):
		"""Returns the color of the current vertex."""

		return self.color

class Queue(object):
	"""Represents a queue ADT."""

	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

class Stack(object):
	"""Represents a stack ADT."""

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

def bfs(graph, vertex_1):
	"""Checks for whether vertex_2 is accessible from vertex_1 in graph."""

	vertex_q = Queue()
	vertex_q.enqueue(vertex_1)

	while vertex_q.size() > 0:
		current_v = vertex_q.dequeue()
		current_v.set_color('gray')
		for nbr in current_v.get_connections():
			if nbr.get_color() == 'white':
				vertex_q.enqueue(nbr)
				nbr.set_dist(current_v.get_dist() + 1)
				nbr.set_pred(current_v)
		current_v.set_color('black')

def bfs_path(graph, vertex_1, vertex_2):
	"""Returns a bfs path from vertex 1 to vertex 2."""

	bfs(graph, vertex_1)
	current = vertex_2
	path = [current]
	while current.get_pred() is not None:
		path.insert(0, current.get_pred())
		current = current.get_pred()
	return [v.get_data() for v in path]

def dfs_path(graph, vertex_1, vertex_2):
	"""Returns a list of all paths from vertex_1 to vertex_2 or None."""

	vertex_stack = Stack()
	vertex_stack.push(vertex_1)
	visited = []
	found = False

	while vertex_stack.size() > 0 and not found:
		current_v = vertex_stack.pop()
		visited.append(current_v)
		for nbr in current_v.get_connections():
			if nbr == vertex_2:
				visited.append(nbr)
				found = True
			if nbr not in visited:
				vertex_stack.push(nbr)
		
	if found:
		return [i.get_data() for i in visited]
	else:
		return None


