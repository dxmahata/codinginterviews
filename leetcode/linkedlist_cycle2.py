'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

URL: https://leetcode.com/problems/linked-list-cycle-ii/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None:    
            return None
        
        slower = head   # Move one step each time
        quicker = head  # Move two steps each time
        
        while quicker.next != None and quicker.next.next != None:
            slower = slower.next
            quicker = quicker.next.next
            
            # The slower and quicker meet with each other. There is a cycle.
            if slower == quicker:   
                break
            else:
                # quicker reach the end. Limited list never have cycle.
                return None
        
        # Both latter and former move one step in each round, until they meet.
        # The meeting place is the entry point of cycle.
        latter, former = head, quicker
        while latter != former:
            latter = latter.next
            former = former.next
        
        return former   
