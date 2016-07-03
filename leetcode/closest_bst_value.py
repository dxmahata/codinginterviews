"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min_dif = float("inf")
        closestVal = None
        
        if root == None:
            return None
        else:
            while root:
                root_val = root.val
                val_dif = abs(root_val - target)
                if val_dif < min_dif:
                    min_dif = val_dif
                    closestVal = root_val
                if target < root_val:
                    if root.left != None:
                        root = root.left
                    else:
                        root = None
                else:
                    if root.right != None:
                        root = root.right
                    else:
                        root = None
        return closestVal
                    
                
                
                    
        