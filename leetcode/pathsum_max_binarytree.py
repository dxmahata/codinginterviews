"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node 
to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""
import sys
class Solution:
    def __init__(self):
        self.max_sum = -sys.maxsize - 1
        
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        self.maxSum(root)
        
    def maxSum(self, root):
        if root == None:
            return 0
        left = self.maxSum(root.left)
        right = self.maxSum(root.right)
        self.max_sum = max(root.val + left + right, self.max_sum)
        ret = root.val + max(left, right)
        if ret < 0:
            return 0
        else:
            return ret
        
