'''
Given a list of words and two words word1 and word2, return the shortest distance 
between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

URL: https://leetcode.com/problems/shortest-word-distance/
'''

import sys
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        word2_positions = []
        word1_positions = []
        
        for i in range(len(words)):
            if word1 == words[i]:
                word1_positions.append(i)
            if word2 == words[i]:
                word2_positions.append(i)
                
        min_dist = sys.maxsize
        
        for pos1 in word1_positions:
            for pos2 in word2_positions:
                if abs(pos1 - pos2) < min_dist:
                    min_dist = abs(pos1 - pos2)
                    
        return min_dist