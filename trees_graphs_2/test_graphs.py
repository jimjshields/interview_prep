import unittest
from graphs import *

class TestGraph(unittest.TestCase):
	"""Tests the representation of the directed graph ADT."""

	def setUp(self):
		"""Starts each test with an empty graph."""

		self.graph = Graph()

	def test_init(self):
		"""Tests that it initializes correctly."""

		self.assertEqual(self.graph.vertices, [])

	def test_add_vertex(self):
		vertex = Vertex(1)
		self.graph.add_vertex(vertex)
		self.assertEqual(self.graph.vertices, [vertex])

	def test_get_vertices(self):
		vertex = Vertex(1)
		self.graph.add_vertex(vertex)
		self.assertEqual(self.graph.get_vertices(), [vertex])

	def test_add_edge(self):
		vertex_1 = Vertex(1)
		vertex_2 = Vertex(2)
		self.graph.add_edge(vertex_1, vertex_2)
		self.assertEqual(vertex_1.connections, [vertex_2])

class TestUndirectedGraph(unittest.TestCase):
	"""Tests the representation of the undirected graph ADT."""

	def setUp(self):
		"""Starts each test with an empty graph."""

		self.u_graph = UndirectedGraph()

	def test_init(self):
		"""Tests that it initializes correctly."""

		self.assertEqual(self.u_graph.vertices, [])

	def test_add_edge(self):
		vertex_1 = Vertex(1)
		vertex_2 = Vertex(2)
		self.u_graph.add_edge(vertex_1, vertex_2)
		self.assertEqual(vertex_1.connections, [vertex_2])
		self.assertEqual(vertex_2.connections, [vertex_1])


class TestVertex(unittest.TestCase):
	"""Tests the representation of the vertex ADT."""

	def setUp(self):
		self.vertex = Vertex(1)

	def test_init(self):
		self.assertEqual(self.vertex.data, 1)
		self.assertEqual(self.vertex.connections, [])
		self.assertEqual(self.vertex.pred, None)
		self.assertEqual(self.vertex.dist, 0)

	def test_add_connection(self):
		vertex_2 = Vertex(2)
		self.vertex.add_connection(vertex_2)
		self.assertEqual(self.vertex.connections, [vertex_2])

	def test_get_data(self):
		self.assertEqual(self.vertex.get_data(), 1)

	def test_get_connections(self):
		vertex_2 = Vertex(2)
		self.vertex.add_connection(vertex_2)
		self.assertEqual(self.vertex.get_connections(), [vertex_2])

	def test_set_dist(self):
		self.vertex.set_dist(1)
		self.assertEqual(self.vertex.get_dist(), 1)

	def test_set_pred(self):
		self.vertex_2 = Vertex(2)
		self.vertex_2.set_pred(self.vertex)
		self.assertEqual(self.vertex_2.get_pred(), self.vertex)

class TestQueue(unittest.TestCase):
	"""Tests the representation of the queue ADT."""

	def setUp(self):
		self.queue = Queue()

	def test_enqueue(self):
		self.queue.enqueue(1)
		self.assertEqual(self.queue.items, [1])

	def test_dequeue(self):
		self.queue.enqueue(1)
		self.assertEqual(self.queue.dequeue(), 1)

	def test_size(self):
		self.queue.enqueue(1)
		self.assertEqual(self.queue.size(), 1)

	def test_is_empty(self):
		self.assertTrue(self.queue.is_empty())

class TestStack(unittest.TestCase):
	"""Tests the representation of the stack ADT."""

	def setUp(self):
		self.stack = Stack()

	def test_push(self):
		self.stack.push(1)
		self.assertEqual(self.stack.items, [1])

	def test_pop(self):
		self.stack.push(1)
		self.assertEqual(self.stack.pop(), 1)

	def test_size(self):
		self.stack.push(1)
		self.assertEqual(self.stack.size(), 1)

	def test_is_empty(self):
		self.assertTrue(self.stack.is_empty())

class TestSearch(unittest.TestCase):
	"""Tests whether search algorithm implementations work."""

	def setUp(self):
		self.graph = Graph()
		self.va = Vertex('A')
		self.vb = Vertex('B')
		self.vc = Vertex('C')
		self.vd = Vertex('D')
		self.ve = Vertex('E')
		self.graph.add_edge(self.va, self.vb)
		self.graph.add_edge(self.va, self.vc)
		self.graph.add_edge(self.va, self.vd)
		self.graph.add_edge(self.vd, self.vb)
		self.graph.add_edge(self.vd, self.vd)
		self.graph.add_edge(self.vd, self.ve)
		self.graph.add_edge(self.ve, self.va)

		self.graph_2 = UndirectedGraph()
		self.v1 = Vertex(1)
		self.v2 = Vertex(2)
		self.v3 = Vertex(3)
		self.v4 = Vertex(4)
		self.v5 = Vertex(5)
		self.v6 = Vertex(6)
		self.v7 = Vertex(7)
		self.v8 = Vertex(8)
		self.v9 = Vertex(9)
		self.v10 = Vertex(10)
		self.v11 = Vertex(11)
		self.v12 = Vertex(12)
		self.v13 = Vertex(13)
		self.graph_2.add_edge(self.v1, self.v4)
		self.graph_2.add_edge(self.v1, self.v2)
		self.graph_2.add_edge(self.v4, self.v7)
		self.graph_2.add_edge(self.v2, self.v3)
		self.graph_2.add_edge(self.v2, self.v5)
		self.graph_2.add_edge(self.v5, self.v6)
		self.graph_2.add_edge(self.v5, self.v8)
		self.graph_2.add_edge(self.v6, self.v10)
		self.graph_2.add_edge(self.v6, self.v9)
		self.graph_2.add_edge(self.v10, self.v11)
		self.graph_2.add_edge(self.v9, self.v12)

		self.graph_3 = UndirectedGraph()
		self.v1a = Vertex(1)
		self.v2a = Vertex(2)
		self.v3a = Vertex(3)
		self.v4a = Vertex(4)
		self.v5a = Vertex(5)
		self.v6a = Vertex(6)
		self.v7a = Vertex(7)
		self.v8a = Vertex(8)
		self.v9a = Vertex(9)
		self.v10a = Vertex(10)
		self.v11a = Vertex(11)
		self.v12a = Vertex(12)
		self.v13a = Vertex(13)
		self.v14a = Vertex(14)
		self.graph_3.add_edge(self.v1a, self.v2a)
		self.graph_3.add_edge(self.v1a, self.v4a)
		self.graph_3.add_edge(self.v4a, self.v5a)
		self.graph_3.add_edge(self.v4a, self.v7a)
		self.graph_3.add_edge(self.v7a, self.v13a)
		self.graph_3.add_edge(self.v13a, self.v14a)
		self.graph_3.add_edge(self.v14a, self.v8a)
		self.graph_3.add_edge(self.v8a, self.v5a)
		self.graph_3.add_edge(self.v5a, self.v2a)
		self.graph_3.add_edge(self.v2a, self.v3a)
		self.graph_3.add_edge(self.v3a, self.v11a)
		self.graph_3.add_edge(self.v11a, self.v10a)
		self.graph_3.add_edge(self.v10a, self.v6a)
		self.graph_3.add_edge(self.v6a, self.v5a)
		self.graph_3.add_edge(self.v6a, self.v9a)
		self.graph_3.add_edge(self.v9a, self.v12a)

	def test_bfs(self):
		bfs(self.graph, self.va)
		self.assertEqual(self.ve.get_color(), 'black')
		self.assertEqual(self.va.get_dist(), 0)
		self.assertFalse(self.ve.get_dist() == 1)

	def test_bfs_2(self):
		bfs(self.graph_2, self.v1)
		self.assertEqual(self.v1.get_color(), 'black')
		self.assertEqual(self.v1.get_dist(), 0)
		self.assertFalse(self.v10.get_dist() == 1)
		self.assertTrue(self.v10.get_dist() == 4)

	def test_bfs_return_path(self):
		path_2 = bfs_path(self.graph_2, self.v7, self.v12)
		self.assertEqual([7, 4, 1, 2, 5, 6, 9, 12], path_2)

	def test_bfs_return_path_2(self):
		path = bfs_path(self.graph_2, self.v1, self.v10)
		self.assertEqual([1, 2, 5, 6, 10], path)

	def test_bfs_return_path_3(self):
		path = bfs_path(self.graph_2, self.va, self.ve)
		self.assertEqual(['A', 'D', 'E'], path)

	def test_bfs_return_path_4(self):
		path = bfs_path(self.graph_3, self.v1a, self.v12a)
		self.assertEqual([1, 4, 5, 6, 9, 12], path)

if __name__ == '__main__':
	unittest.main()