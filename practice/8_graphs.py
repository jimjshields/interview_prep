# Implement a graph ADT
# http://en.wikipedia.org/wiki/Graph_%28abstract_data_type%29
# http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/Graphs.html

# Definition of a graph: collection of vertices connected by edges
# Separate from a tree in that there is not a single root node to which all vertices trace back their ancestry
# Can be any set of relationships
# Can be directed - one-way edges - or two-way
# Can have weights to get from one vertex to another (cost of the edge)
# Cycles - paths that start and end at the same vertex
# Graph w/ no cycles - acyclic; directed acyclic - aka DAG - special algos
# Usually the vertices are drawn from some related type/set

# Forgot - ids, string repr, making connections/vertices a dict, counting # of vertices

class Vertex(object):
	"""A vertex in a graph."""

	def __init__(self, key):
		"""Initializes a vertex with a given data payload."""

		self.id = key
		self.connections = {}

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

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_edge(1, 5, 10)
g.add_edge(1, 20, 10)
g.add_edge(1, 2200, 234)
print g.get_vertices()