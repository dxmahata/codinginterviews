"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node 
down to the nearest leaf node.

URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None:
            return self.minDepth(root.right) + 1
        elif root.right == None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right)) + 1
        
        

        