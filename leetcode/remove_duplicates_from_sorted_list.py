"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head == None:
            return None
        else:
            current = head
            while current != None and current.next != None:
                if current.val == current.next.val:
                    temp = current.next
                    current.next = current.next.next
                    del temp
                else:
                    current = current.next
                    
            return head