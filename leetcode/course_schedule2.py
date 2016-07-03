"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to 
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the 
ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If 
it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have 
finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have 
finished both courses 1 and 2. Both courses 1 and 2 should be taken after you 
finished course 0. So one correct course order is [0,1,2,3]. Another correct 
ordering is[0,2,1,3].
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
    
    
class Solution:
    def __init__(self):
        self.has_cycle = False
        
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if prerequisites == [] and numCourses > 0:
            return [entries for entries in range(numCourses)]
        elif prerequisites == [] and numCourses == 0:
            return []
        else:            
            G = DirectedGraph()
            for entries in prerequisites:
                G.addEdge(entries[1], entries[0], 1)
                        
            return self.topsort(G)
            
    
    def topsort(self, G):
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
                self.has_cycle = True
            
            return topological_list
        
#     def get_extra_courses(self, numCourses, prerequisites):
#         courses = []
#         for entries in prerequisites:
#             courses.append(entries[0])
#             courses.append(entries[1])
#             
#         unique_courses = len(set(courses))
#         if numCourses > unique_courses:
#             extra_courses = set([entries for entries in range(numCourses)]).difference(set(courses))
#             return list(extra_courses)
#         return 0        

if __name__ == "__main__":
    
    soln = Solution()
    print(soln.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(soln.findOrder(2, [[1,0]]))
    print(soln.findOrder(3, [[1,0]]))
    #print(soln.findOrder(10, [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]))