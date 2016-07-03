"""
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
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
    def levelOrder(self, root):
        if root == None:
            return []
        else:
            q = Queue()
            q.put(root)
            q.put("#")
            levelOrderTraversal = []
            level = []
            while q.empty() == False:
                node = q.get()
                if node == "#":
                    if q.empty() == False:
                        q.put("#")
                    levelOrderTraversal.append(level)
                    level = []
                else:
                    level.append(node.val)
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)
                        
            return levelOrderTraversal
        