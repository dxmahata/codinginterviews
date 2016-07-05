'''
Merge two sorted linked lists and return it as a new list. The new list should 
be made by splicing together the nodes of the first two lists.

URL: https://leetcode.com/problems/merge-two-sorted-lists/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        else:
            if l1 == None:
                return l2
            if l2 == None:
                return l1
                
            if l1.val <= l2.val:
                result = l1
                result.next = self.mergeTwoLists(l1.next,l2)
            else:
                result = l2
                result.next = self.mergeTwoLists(l1, l2.next)
                
            return result
