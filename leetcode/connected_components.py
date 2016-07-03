"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge 
is a pair of nodes), write a function to find the number of connected components in an undirected graph.

URL : https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""

import sys
from queue import Queue

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited        
        self.visited = False
        # Mark all nodes color with white        
        self.color = 'white'      
        # Predecessor
        self.previous = None

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()  

    def getVertexID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color    

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None

    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 1 and edges == []:
            return 1
        else:
            G = Graph()
            for entries in edges:
                G.addEdge(entries[0], entries[1], 1)
            count = 0
            for vertex in G:
                if vertex.getColor() == "white":
                    count += 1
                    self.bfs(vertex)
                    
            return count

    def bfs(self, vertex):
        vertex.setColor("gray")
        q = Queue()
        q.put(vertex)
        while q.empty() == False:
            curr_node = q.get()
            for nbr in curr_node.getConnections():
                if nbr.getColor() == "white":
                    nbr.setColor("gray")
                    q.put(nbr)
            curr_node.setColor("black")
                
        
if __name__ == "__main__":
    
    n = 5
    edges1 = [[0, 1], [1, 2], [3, 4]]
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    
    soln = Solution()
    print(soln.countComponents(n, edges1))
    print(soln.countComponents(n, edges2))