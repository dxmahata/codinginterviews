"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

URL: https://leetcode.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        else:
            hare = head
            tortoise = head
            
            while (hare != None and tortoise != None):
                hare = hare.next
                if hare == tortoise:
                    return True
                
                if hare == None:
                    return False
                
                hare = hare.next
                
                if hare == tortoise:
                    return True
                    
                torotoise = tortoise.next
            return False