"""
Reverse a singly linked list.

URL: https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None:
            return None
        else:
            temp = None
            while head != None:
                nextNode = head.next
                head.next = temp
                temp = head
                head = nextNode
                
            return temp
                
                
        