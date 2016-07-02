'''
Created on Jul 1, 2016

@author: Debanjan
'''
from queue import Queue
import sys

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

def topsort(G):
    if G.getVertices() == []:
        return []
    else:
        topological_list = []
        topological_queue = Queue()
        nodes = G.getVertices()
        for node in G:
            if node.getIndegree() == 0:
                topological_queue.put(node)
                
        while topological_queue.empty() == False:
            curr_node = topological_queue.get()
            topological_list.append(curr_node.getVertexID())
            
            for nbr in curr_node.getConnections():
                nbr.setIndegree(nbr.getIndegree() - 1)
                if nbr.getIndegree() == 0:
                    topological_queue.put(nbr)
                    
        if len(topological_list) != len(nodes):
            return "The given graph has a cycle"
        
        return ">".join(topological_list)
                
                
if __name__ == "__main__":
    
    DG = DirectedGraph()
    DG.addVertex("a")
    DG.addVertex("b")
    DG.addVertex("c")
    DG.addVertex("d")
    DG.addVertex("e")
    DG.addVertex("f")
    DG.addVertex("g")
    
    DG.addEdge("a", "c", 1)
    DG.addEdge("b", "c", 1)
    DG.addEdge("c", "e", 1)
    DG.addEdge("b", "d", 1)
    DG.addEdge("e", "f", 1)
    DG.addEdge("d", "f", 1)
    DG.addEdge("f", "g", 1)
    #add the following node if you need a cycle in the graph
    #DG.addEdge("g", "b", 1)
    
    print(topsort(DG))