"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
URL: https://leetcode.com/problems/clone-graph/
"""
from queue import Queue

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return node
        else:
            graphHashTable = {}
            clonedNode = UndirectedGraphNode(node.label)
            graphHashTable[node] = clonedNode
            q = Queue()
            q.put(node)
            while q.empty() == False:
                currNode = q.get()
                for nbr in currNode.neighbors:
                    if nbr in graphHashTable:
                        graphHashTable[currNode].neighbors.append(graphHashTable[nbr])
                    else:
                        clonedNbrNode = UndirectedGraphNode(nbr.label)
                        graphHashTable[currNode].neighbors.append(clonedNbrNode)
                        graphHashTable[nbr] = clonedNbrNode
                        q.put(nbr)
            return clonedNode
