"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue
class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if root == None:
            return []
        else:
            q = Queue()
            q.put(root)
            q.put("#")
            levelOrderTraversal = []
            level = []
            stack = []
            
            while q.empty() == False:
                node = q.get()
                if node == "#":
                    if q.empty() == False:
                        q.put("#")
                    stack.append(level)
                    level = []
                else:
                    level.append(node.val)
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)
                        
            while stack:
                levelOrderTraversal.append(stack.pop())
                
            return levelOrderTraversal
        
        