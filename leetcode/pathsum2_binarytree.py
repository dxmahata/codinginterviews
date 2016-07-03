"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum 
equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

URL: https://leetcode.com/problems/path-sum-ii/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        else:
            stack = []
            paths = []
            
            current = root
            stack.append(current)
            stack.append([current.val])
            stack.append(current.val)
            while stack != []:
                pathsum = stack.pop()
                path = stack.pop()
                curr = stack.pop()
                if curr.left == None and curr.right == None:
                    if pathsum == sum:
                        paths.append(path)
                if curr.right:
                    rightstr = path + [curr.right.val]
                    rightsum = pathsum + curr.right.val
                    stack.append(curr.right)
                    stack.append(rightstr)
                    stack.append(rightsum)
                if curr.left:
                    leftstr = path + [curr.left.val]
                    leftsum = pathsum + curr.left.val
                    stack.append(curr.left)
                    stack.append(leftstr)
                    stack.append(leftsum)
            return paths                    