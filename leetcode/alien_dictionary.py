"""
There is a new alien language which uses the latin alphabet. However, 
the order among letters are unknown to you. You receive a list of words 
from the dictionary, where words are sorted lexicographically by the rules 
of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

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
        
        return "".join(topological_list)
    
class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 0:
            return ""
        else:
            G = DirectedGraph()
            for word in words:
                for i in range(len(word)-1):
                    ch_i = word[i]
                    for j in range(i+1, len(word)):
                        ch_j = word[j]
                        G.addEdge(ch_i, ch_j, 1)
            
            return topsort(G)
if __name__ == "__main__":
    
    word_list = ["wrt","wrf","er","ett","rftt"]
    
    soln = Solution()
    
    print(soln.alienOrder(word_list))