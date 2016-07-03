"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
   
URL: https://leetcode.com/problems/symmetric-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isMirror(root.left, root.right)
            
    def isMirror(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        else:
            if root1.val == root2.val:
                return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
            else:
                return False
        
        