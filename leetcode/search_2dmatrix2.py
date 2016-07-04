"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

URL: https://leetcode.com/problems/search-a-2d-matrix-ii/
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
            
            if target < matrix[0][0] or target > matrix[no_rows-1][no_cols-1]:
                return False
            else:
                r = 0
                c = no_cols-1
                
                while r < no_rows and c >=0:
                    if matrix[r][c] == target:
                        return True
                    elif target > matrix[r][c]:
                        r += 1
                    elif target < matrix[r][c]:
                        c -= 1
                return False