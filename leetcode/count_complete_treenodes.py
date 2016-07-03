"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 
1 and 2h nodes inclusive at the last level h.

URL: https://leetcode.com/problems/count-complete-tree-nodes/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            leftHeight = self.getLeftHeight(root) + 1
            rightHeight = self.getRightHeight(root) + 1
            
            if leftHeight == rightHeight:
                return (2<<(leftHeight-1))-1
            else:
                return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
        
    def getLeftHeight(self, root):
        if root == None:
            return 0
        else:
            leftHeight = 0
            while root.left != None:
                leftHeight += 1
                root = root.left
            return leftHeight
            
    def getRightHeight(self, root):
        if root == None:
            return 0
        else:
            rightHeight = 0
            while root.right != None:
                rightHeight += 1
                root = root.right
            return rightHeight
        