"""
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

URL: https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        else:
            no_rows = len(matrix)
            no_cols = len(matrix[0])
            
            #get the first element and the last element of the matrix
            #compare it with the target
            if target < matrix[0][0] or target > matrix[no_rows-1][no_cols-1]:
                return False
                
            r = 0
            c = no_cols - 1
            while r < no_rows and c >= 0:
                if target == matrix[r][c]:
                    return True
                elif target > matrix[r][c]:
                    r += 1
                elif target < matrix[r][c]:
                    c -= 1
            return False
                    