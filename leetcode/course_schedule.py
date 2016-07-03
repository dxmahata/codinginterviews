"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first 
take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible 
for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished 
course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished 
course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency 
matrices. Read more about how a graph is represented.

URL: https://leetcode.com/problems/course-schedule/
"""

class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.adjacent = {}
        self.indegree = 0
        self.outdegree = 0
        self.predecessor = None
        self.visit_time = 0
        self.finish_time = 0
        self.color = "white"
        
    def add_neighbor(self, nbr, weight=0):
        self.adjacent[nbr] = weight
        
    def get_neighbors(self):
        return self.adjacent.keys()
    
    def get_id(self):
        return self.id
    
    def get_weight(self, nbr):
        return self.adjacent[nbr]
    
    def get_indegree(self):
        return self.indegree
    
    def set_indegree(self, indegree):
        self.indegree = indegree
    
    def get_outdegree(self):
        return self.outdegree
    
    def set_outdegree(self, outdegree):
        self.outdegree = outdegree
    
    def get_predecessor(self):
        return self.predecessor
    
    def set_predecessor(self, pred):
        self.predecessor = pred
    
    def get_visit_time(self):
        return self.visit_time
    
    def set_visit_time(self, visit_time):
        self.visit_time = visit_time
    
    def get_finish_time(self):
        return self.finish_time
    
    def set_finish_time(self, finish_time):
        self.finish_time = finish_time
        
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.adjacent])

        
    

class Graph:
    
    def __init__(self):
        self.vertex_dict = {}
        self.no_vertices = 0
        self.no_edges = 0
        
    def add_vertex(self, vert_key):
        new_vertex_obj = Vertex(vert_key)
        self.vertex_dict[vert_key] = new_vertex_obj
        self.no_vertices += 1
    
    def get_vertex(self, vert_key):
        if vert_key in self.vertex_dict:
            return self.vertex_dict[vert_key]
        else:
            return None
    
    def add_edge(self, fro, to, weight=1):
        if fro not in self.vertex_dict:
            self.add_vertex(fro)
            from_vertex = self.get_vertex(fro)
        else:
            from_vertex = self.vertex_dict[fro]
            
        if to not in self.vertex_dict:
            self.add_vertex(to)
            to_vertex = self.get_vertex(to)
        else:
            to_vertex = self.vertex_dict[to]
            
        from_vertex.add_neighbor(to_vertex, weight)
        from_vertex.set_outdegree(from_vertex.get_outdegree() + 1)
        to_vertex.set_indegree(to_vertex.get_indegree() + 1)
        self.no_edges += 1
    
    def get_edges(self):
        edges = []
        for u in self.vertex_dict:
            for v in self.vertex_dict[u].get_neighbors():
                u_id = u
                #print(v)
                v_id = v.get_id()
                edges.append((u_id, v_id, self.vertex_dict[u].get_weight(v)))
        return edges
    
    def get_vertices(self):
        return self.vertex_dict
        
        
class DFS:
    
    def __init__(self, graph):
        self.graph = graph
        self.has_cycle = False
        
    def dfs(self):
        for vertex in self.graph.get_vertices():
            if self.graph.vertex_dict[vertex].get_color() == "white":
                self.dfs_visit(self.graph.vertex_dict[vertex])
                
    def dfs_visit(self, node):
        node.set_color("gray")
        for vert in node.get_neighbors():
            if vert.get_color() == "gray":
                self.has_cycle = True
            if vert.get_color() == "white":
                vert.set_color("gray")
                vert.set_predecessor(node)
                self.dfs_visit(vert)
        node.set_color("black")
                

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        else:
            g = Graph()
            
            for edge in prerequisites:
                g.add_edge(edge[0], edge[1])
                
            dfs_obj = DFS(g)
            dfs_obj.dfs()
            if dfs_obj.has_cycle == True:
                return False
            else:
                return True
            
            
if __name__ == "__main__":
    soln1 = Solution()
    print(soln1.canFinish(2, [[1,0]]))
    
    soln2 = Solution()
    print(soln2.canFinish(2, [[1,0],[0,1]]))