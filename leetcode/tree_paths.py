"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root == None:
            return []
        else:
            paths = []
            current = root
            s = []
            s.append(current)
            s.append(str(current.val))
            
            while s != []:
                path = s.pop()
                current = s.pop()
                if not current.left and not current.right:
                    paths.append(path)
                if current.right:
                    rightstr = path + "->" + str(current.right.val)
                    s.append(current.right)
                    s.append(rightstr)
                if current.left:
                    leftstr = path + "->" + str(current.left.val)
                    s.append(current.left)
                    s.append(leftstr)
            return paths
                    
        