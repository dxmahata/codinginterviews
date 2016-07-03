"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            stack = []
            paths = []
            stack.append(root)
            stack.append(str(root.val))
            while stack != []:
                path = stack.pop()
                current = stack.pop()
                if current.left == None and current.right == None:
                    paths.append(int(path))
                if current.right:
                    rightstr = path + str(current.right.val)
                    stack.append(current.right)
                    stack.append(rightstr)
                if current.left:
                    leftstr = path + str(current.left.val)
                    stack.append(current.left)
                    stack.append(leftstr)
            return sum(paths)
                    
        