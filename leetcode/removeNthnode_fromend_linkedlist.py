'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):

        former = head
        latter = head
 
        # Skip n-1 nodes with latter
        for _ in range(n-1):   
            latter = latter.next
 
        if latter.next == None:
            # There are totally n nodes. And we are
            # removing the head node.
            head = head.next
        else:
            # There are more than n nodes.
            latter = latter.next    # Totally skip n nodes
 
            # Find the previous node to the nth node from end
            while latter.next != None:
                former = former.next
                latter = latter.next
 
            # Remove the nth node from end
            former.next = former.next.next
 
        return head