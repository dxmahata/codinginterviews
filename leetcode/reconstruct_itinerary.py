"""Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

https://leetcode.com/problems/reconstruct-itinerary/
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self.elements = {}
        
    def push(self, item):
        heapq.heappush(self._queue, item)
        self.elements[item] = 1
        
    def pop(self):
        return heapq.heappop(self._queue)
        
    def empty(self):
        if self._queue == []:
            return True
        else:
            return False
            
    def __contains__(self, item):
        return item in self.elements
        
class Solution(object):
    def __init__(self):
        self.map = {}
        self.result = []
    
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        for entries in tickets:
            fro = entries[0]
            to = entries[1]
            if fro in self.map:
                self.map[fro].push(to)
            else:
                pq = PriorityQueue()
                self.map[fro] = pq
                self.map[fro].push(to)
        
        self.dfs("JFK")
        self.result.reverse()
        return self.result
        
    def dfs(self, s):
        try:
            q = self.map[s]
        except KeyError:
            q = None
            
        while q != None and q.empty() == False:
            curr_node = q.pop()
            self.dfs(curr_node)
        self.result.append(s)
                
if __name__ == "__main__":
    
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    soln = Solution()
    result = soln.findItinerary(tickets)
    print(result)