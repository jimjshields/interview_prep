class Graph(object):
	"""Represents a graph ADT."""

	def __init__(self):
		self.vertices = []

	def add_edge(self, data_1, data_2, cost):
		if not self.get_vertex_from_data(data_1):
			v_1 = Vertex(data_1)
			self.vertices.append(v_1)
		else:
			v_1 = self.get_vertex_from_data(data_1)
		if not self.get_vertex_from_data(data_2):
			v_2 = Vertex(data_2)
			self.vertices.append(v_2)
		else:
			v_2 = self.get_vertex_from_data(data_2)
		v_1.add_connection(v_2, cost)

	def get_vertices(self):
		return self.vertices

	def get_data(self):
		return [vertex.data for vertex in self.vertices]

	def get_vertex_from_data(self, data):
		for v in self.vertices:
			if v.data == data:
				return v
		else: 
			return None

	def __contains__(self, data):
		return data in self.get_data()


class Vertex(object):
	"""Vertex in a graph."""

	def __init__(self, data):
		self.data = data
		self.connections = []
		self.cost = 0

	def add_connection(self, other, cost):
		self.connections.append((other, cost))

	def get_connections(self):
		return self.connections

	def set_new_cost(self, cost):
		self.cost = cost

	def get_cost(self):
		return self.cost


n,l = map(int,raw_input().split())
graph = Graph()

for i in xrange(l):
	a, b, cost = map(int,raw_input().split())
	graph.add_edge(a, b, cost)

def find_cheapest_route(graph, start, end):
	"""Given a graph with a cost for each edge, return the cheapest cost from start to end."""

	costs = []
	vertex_stack = [graph.get_vertex_from_data(start)]

	while vertex_stack != []:
		current = vertex_stack.pop()
		for v in current.get_connections():
			vertex_stack.append(v[0])
			if current.cost < v[1]:
				v[0].set_new_cost(v[1])
			else:
				v[0].set_new_cost(current.cost)
			if v[0].data == end:
				costs.append(v[0].get_cost())

	return min(costs)