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
findPath(g2, 1, 100)

# def bfs(start, paths):
# 	for i in graph[start[-1]]:
# 		path = start + [i]
# 		if start not in paths:
# 			paths.append(start)
