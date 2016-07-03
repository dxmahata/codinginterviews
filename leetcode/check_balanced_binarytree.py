"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    
    def getHeight(self, root):
        if root == None:
            return 0
        
        leftHeight = self.getHeight(root.left)
        if leftHeight == -1:
            return -1
            
        rightHeight = self.getHeight(root.right)
        if rightHeight == -1:
            return -1
            
        heightDiff = abs(leftHeight - rightHeight)
        if heightDiff > 1:
            return -1
        else:
            return max(leftHeight,rightHeight)+1
            
        
    def isBalanced(self, root):
        if self.getHeight(root) == -1:
            return False
        else:
            return True
        