"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3 
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
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
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        else:
            q = Queue()
            q.put(root)
            q.put("#")
            levelOrderTraversal = []
            level = []
            levelNo = 0
            while q.empty() == False:
                node = q.get()
                if node == "#":
                    if q.empty() == False:
                        q.put("#")
                    if levelNo == 0 or levelNo % 2 == 0:    
                        levelOrderTraversal.append(level)
                    else:
                        levelOrderTraversal.append(level[::-1])
                    level = []
                    levelNo += 1
                else:
                    level.append(node.val)
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)
                        
            return levelOrderTraversal
                        
            
        