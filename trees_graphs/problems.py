# 1 

# a - what's a graph? what's a tree?
# graph - abstract data type (adt) - set of vertices and edges connected to one another
# tree - adt - where there is one root node and each node only has one parent

# b - describe a directed vs. undirected graph
# directed - all of the edges are one-way - going in a single direction
# undirected - any edge is two-way

# c represent a graph somehow in python

# class/dict representation - from http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
class Vertex(object):
	"""Creates a vertex in a graph."""
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return "%s connected to %s" % (self.id, str([x.id for x in self.connectedTo])) 

	def getConnections(self):
		return self.connectedTo.keys()

	def getID(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

class Graph(object):
	"""Creates a graph."""
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self, n):
		return n in self.vertList

	def addEdge(self, f, t, cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv - self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

g = Graph()

g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('D', 'B')
g.addEdge('D', 'D')
g.addEdge('D', 'E')
g.addEdge('E', 'A')

# for v in g:
# 	print v

# diff implementation - adjacency list

gDict = {'A': ['B', 'C', 'D'],
		 'B': [],
		 'C': [],
		 'D': ['B', 'D', 'E'],
		 'E': ['A']}

# d - write a function that, given a graph and two nodes, tells if the second node is accessible from the first

# class function
def isConnected(graph, node1, node2):
	node1 = g.getVertex(node1)
	node2 = g.getVertex(node2)
	return node2 in node1.getConnections()

# print isConnected(g, 'A', 'E')

# dict function
def isConnectedDict(graph, node1, node2):
	return node2 in graph[node1]

# print isConnectedDict(gDict, 'A', 'E')

# 2 - with a given graph, write a program that finds a path from 1 to 10
g = [[], 		# 0
     [2, 4], 	# 1
     [1, 3, 5], # 2
     [2],		# 3
     [1, 7],	# 4
     [2, 6, 8],	# 5
     [5, 9, 10],# 6
     [4],		# 7
     [5],		# 8
     [6, 12],	# 9
     [6, 11],	# 10
     [10],		# 11
     [9],		# 12
     []]		# 13

import random

def findPath(graph, node1, node2, path=[]):
	currentNode = node1
	if node2 in graph[currentNode]:
		path.append(currentNode)
		path.append(node2)
		print "Path: %s; Length: %s" % (path, len(path))
	else:
		path.append(currentNode)
		for i in graph[currentNode]:
			if i not in path:
				currentNode = i
				break
		else:
			randNum = random.randint(0, len(graph[currentNode]) - 1)
			currentNode = graph[currentNode][randNum]
		findPath(graph, currentNode, node2)

g2 = [[],
	  [2, 4],
	  [1, 3, 5],
	  [2, 11],
	  [1, 5, 7],
	  [2, 4, 6, 8],
	  [5, 9, 10],
	  [4, 13],
	  [5, 14],
	  [6, 12],
	  [6, 11],
	  [3, 10],
	  [9],
	  [7, 14],
	  [8, 13]]

# findPath(g, 10, 1)
# findPath(g2, 1, 100)

# other implementation - http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/s

graph = {'A': set(['B', 'C']),
		 'B': set(['A', 'D', 'E']),
		 'C': set(['A', 'F']),
		 'D': set(['B']),
		 'E': set(['B', 'F']),
		 'F': set(['C', 'E']),
		 'G': set(),
		 'H': set('G')}

# all connections, no recursion
def dfs(graph, start):
	"""Inputs: graph (implemented as dictionary, keys are nodes and values sets of connections),
			   starting node (string)
	   Output: set of all possible connections from start"""
	# visited will be set of every node that's been visited; stack is what hasn't been explored
	visited, stack = set(), [start]
	# while there's something in the stack
	while stack:
		# vertex is the last value in the stack
		vertex = stack.pop()
		# if it hasn't been visited, add it to visited and add its connections to the stack
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
			# start again until there's nothing in the stack
	# return everything that's a connection
	return visited

# all connections, recursion
def dfs_recur(graph, start, visited=None):
	"""Inputs: graph (implemented as dictionary, keys are nodes and values sets of connections),
			   starting node (string)
	   Output: set of all possible connections from start"""
	if visited is None:
		visited = set()
	visited.add(start)
	for next in graph[start] - visited:
		print visited
		dfs_recur(graph, next, visited)
	return visited

# all paths - still a little confused
def dfs_paths(graph, start, goal):
	"""Inputs: graph (dictionary), start (key - node), goal(key - node)
	   Outputs: all possible paths from start to goal in graph"""
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		# print (vertex, path)
		for next in graph[vertex] - set(path):
			print stack
			if next == goal:
				yield path + [next]
			else:
				stack.append((next, path + [next]))

def bfs(graph, start):
	"""Inputs: graph (dict), starting node (key)
	   Output: all possible connections (set)"""
	visited, queue = set(), [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited

graph = {'A': set(['B', 'C']),
		 'B': set(['A', 'D', 'E']),
		 'C': set(['A', 'F']),
		 'D': set(['B']),
		 'E': set(['B', 'F']),
		 'F': set(['C', 'E']),
		 'G': set(),
		 'H': set('G')}


def bfs_paths(graph, start, goal):
	"""Inputs: graph (dict), start (key - node), goal (key - node)
	   Output: generator of all possible paths from start to goal, beginning w/ the shortest"""
	queue = [(start, [start])]
	# queue includes the first node and the current path
	visited = set()
	# instantiate visited as an empty set
	while queue:
		# while there's something in the queue
		(vertex, path) = queue.pop(0)
		# get rid of the current vertex and path and set it to variables
		for next in graph[vertex] - set(path):
			# for every node we haven't visited yet
			if next == goal:
				# if it's the last one
				yield path + [next]
				# finish and yield the current path and the goal node
			else:
				queue.append((next, path + [next]))
				# otherwise, add the next node and the path and the next node to the queue

def shortest_path(graph, start, goal):
	"""Inputs: graph (dict), start (key - node), goal (key - node)
	   Output: generator of shortest possible path b/w start and goal"""
	try:
		# if there's something yielded by bfs_paths, return the first one
		return next(bfs_paths(graph, start, goal))
	except StopIteration:
		# if not, return None
		return None