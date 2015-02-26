# Knight's tour problem - how does the knight piece visit every square on the
# chessboard?

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

	def set_color(self, color):
		"""Sets the color of the current vertex."""

		self.color = color

	def get_color(self):
		"""Returns the color of the current vertex."""

		return self.color

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

def knight_graph(board_size):
	"""Creates and returns a graph of possible moves for a knight on a board."""

	kt_graph = Graph()
	for row in xrange(board_size):
		for column in xrange(board_size):
			print row, column
			node_id = pos_to_node_id(row, column, board_size)
			new_positions = gen_legal_moves(row, column, board_size)
			for e in new_positions:
				n_id = pos_to_node_id(e[0], e[1], board_size)
				kt_graph.add_edge(node_id, n_id)
	return kt_graph

def gen_legal_moves(x, y, board_size):
	"""Returns a list of the legal moves for the knight given coordinates and
	   board size."""
	new_moves = []
	move_offsets = [(-1, -2), (-1, 2), (1, -2), (1, 2), 
					(-2, -1), (-2, 1), (2, -1), (2, 1)]
	for i in move_offsets:
		new_x = x + i[0]
		new_y = y + i[1]
		if legal_coord(new_x, board_size) and legal_coord(new_y, board_size):
			new_moves.append((new_x, new_y))
	return new_moves

def legal_coord(c, board_size):
	"""Boolean for checking if a coordinate is legal given board size."""

	return (c < board_size and c >= 0)

def pos_to_node_id(row, column, board_size):
	"""Converts a given position on the board to a node id."""

	return (row * board_size) + column

def knight_tour(depth, path, vertex, limit):
	"""Recursively checks for a valid knight's tour path."""

	vertex.set_color('gray')
	path.append(vertex)
	if depth < limit:
		nbr_list = list(vertex.get_connections)
		i = 0
		done = False
		while i < len(nbr_list) and not done:
			if nbr_list[i].get_color() == 'white':
				done = knight_tour(depth + 1, path, nbr_list[i], limit)
			i += 1
		if not done: # prepare to backtrack
			path.pop()
			vertex.set_color('white')
	else:
		done = True
	return done

knight_graph = knight_graph(8)
print knight_graph
# print knight_tour(0, path, A, 6)