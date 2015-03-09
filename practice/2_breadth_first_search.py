# Implement a breadth-first search
# Assume that a graph and queue ADT exist

def breadth_first_search(graph, start):
	"""Traverses a graph breadth-first - level by level.
	   Does this using a queue to store vertices to traverse
	   then by coloring visited vertices gray when they're first visited,
	   and black when all of their children have been visited."""

	# should be 0, not 1
	start.set_dist(0)
	# forgot this
	start.set_pred(None)
	
	# don't set color yet
	
	vertex_queue = Queue()
	vertex_queue.enqueue(start)

	while not vertex_queue.is_empty():
		current_vertex = vertex_queue.dequeue()
		nbrs = current_vertex.get_connections()
		for nbr in nbrs:
			# need to check whether the nbr has been checked - forgot this
			if nbr.get_color() == 'white':
				
				# do these three first, then enqueue
				nbr.set_dist(1 + nbr.get_pred().get_dist())
				nbr.color('gray')
				# forgot this
				nbr.set_pred(current_vertex)

				vertex_queue.enqueue(nbr)
		current_vertex.color('black')

def traverse(y):
	"""Traverese a graph from vertex y."""

	x = y
	while x.get_pred():
		print x.get_data()
		x = x.get_pred()
	print x.get_data()


# Actually implement the graph and vertex classes with those methods

class Vertex(object):
	"""Represents a vertex in a graph."""

	def __init__(self, data):
		"""Starts w/ some given data."""

		self.data = data

	def get_data(self):
		"""Returns the data of the current vertex."""

		return self.data

	def set_pred(self, pred):
		"""Sets the predecessor vertex for the current vertex. Can only have one."""

		self.pred = pred

	def get_pred(self):
		"""Returns the predecessor vertex for the current vertex."""

		return self.pred

	def set_color(self, color):
		"""Set the vertex to a color indicated whether it's been searched: white, gray, or black."""

		self.color = color

	def get_color(self):
		"""Get the color of the current vertex."""

		return self.color

	def set_dist(self, dist):
		"""Set the distance from the start of the current vertex."""

		self.dist = dist

	def get_dist(self):
		"""Get the distance from the start of the current vertex."""

		return self.dist

class Graph(object):
	"""Represents a graph ADT."""

	def __init__(self):
		"""Initializes a graph object."""

		self.head = None

	def add_vertex(self, vertex):
		"""Adds a vertex to the graph."""

from Queue import Queue

def bfs(graph, start):
	"""Searches a graph breadth-first."""

	vertex_q = Queue()
	vertex_q.put(start)

	while vertex_q.qsize() > 0:
		current = vertex_q.get()
		for 