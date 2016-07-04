"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

URL: https://leetcode.com/problems/edit-distance/
"""

class Solution(object):
    def __init__(self):
        self.dist_table = []
        
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (word1 == None or word1 == "") and (word2 == None or word2 == ""):
            return 0
        elif word1 == "":
            return len(word2)
        elif word2 == "":
            return len(word1)
        else:
            m = len(word1)
            n = len(word2)
            self.dist_table = [[0 for j in range(n+1)] for i in range(m+1)]
            no_rows = m + 1
            no_cols = n + 1
            for i in range(0, no_rows):
                for j in range(0, no_cols):
                    if i == 0:
                        self.dist_table[i][j] = j
                    elif j == 0:
                        self.dist_table[i][j] = i
                    elif word1[i-1] == word2[j-1]:
                        self.dist_table[i][j] = self.dist_table[i-1][j-1]
                    else:
                        self.dist_table[i][j] = 1 + min(self.dist_table[i][j-1], self.dist_table[i-1][j], self.dist_table[i-1][j-1])
                        
            return self.dist_table[no_rows-1][no_cols-1]
                        
                    
                    
if __name__ == "__main__":
    soln = Solution()
    print(soln.minDistance("intention", "execution"))