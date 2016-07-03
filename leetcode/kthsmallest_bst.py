"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find 
the kth smallest frequently? How would you optimize the kthSmallest routine?

URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return None
        else:
            stack = []
            node = root
            count = 0
            while stack!= [] or node != None:
                if node != None:
                    stack.append(node)
                    node = node.left
                else:
                    inorder_node = stack.pop()
                    count += 1
                    if count == k:
                        return inorder_node.val
                    node = inorder_node.right
            return None