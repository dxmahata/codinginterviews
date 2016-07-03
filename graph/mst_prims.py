'''
Created on Jul 2, 2016

@author: Debanjan
'''

import sys
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        self._main_items = {}

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._main_items[item] = self._index
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
    def empty(self):
        if self._queue == []:
            return True
        else:
            return False
        
    def __contains__(self, item):
        return item in self._main_items
        
        
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
        #indegree of the vertex
        self.indegree = 0
        
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
        
    def getPrevious(self):
        return self.previous

    def setVisited(self):
        self.visited = True
        
    def setIndegree(self, indegree):
        self.indegree = indegree
        
    def getIndegree(self):
        return self.indegree

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class DirectedGraph:
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
        self.vertDictionary[to].setIndegree(self.vertDictionary[to].getIndegree() + 1)
        
    def getVertices(self):
        return self.vertDictionary.keys()

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous
    
def prims(G, start):
    if G.getVertices() == []:
        return []
    else:
        spanning_tree = []
        pq = PriorityQueue()
        start.setDistance(0)
        start.setPrevious(None)
        for vertex in G:
            pq.push(vertex, vertex.getDistance())
        
        while pq.empty() == False:
            curr_node = pq.pop()
            if curr_node.getVertexID() not in spanning_tree:
                spanning_tree.append(curr_node.getVertexID())
            for nbr in curr_node.getConnections():
                new_dist = curr_node.getWeight(nbr)
                if nbr in pq and new_dist < nbr.getDistance():
                    nbr.setDistance(new_dist)
                    nbr.setPrevious(curr_node)
                    pq.push(nbr, nbr.getDistance())
        
        return spanning_tree
            
def get_shortest_path(start, target):
    path = []
    while target != start:
        path.append(target.getVertexID())
        target = target.getPrevious()
    path.append(start.getVertexID())
    path.reverse()
    return "->".join(path)    
        
if __name__ == "__main__":
    
    G = DirectedGraph()
    
    G.addVertex("a")
    G.addVertex("b")
    G.addVertex("c")
    G.addVertex("d")
    G.addVertex("e")
    
    G.addEdge("a", "c", 1)
    G.addEdge("a", "b", 4)
    G.addEdge("c", "d", 4)
    G.addEdge("c", "b", 2)
    G.addEdge("b", "e", 4)
    G.addEdge("d", "e", 4)
    
    pq = PriorityQueue()
    print(prims(G, G.getVertex("a")))
