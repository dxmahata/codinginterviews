"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

URL: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if root == None:
            return []
        else:
            result = []
            stack = []
            node = root
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    result.append(node.val)
                    node = node.right
            return result
        