'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head == None:
            return head
        else:
            # Compute the length of the list
            listLen = 0
            temp = head
            while temp != None:
                temp = temp.next
                listLen += 1
            
            k = k % listLen
            # No need to rotate
            if k == 0:              
                return head
            
            # Find the last node, and the last (k+1)th node
            former = latter = head
            for _ in range(k):
                latter = latter.next            
            while latter.next != None:
                latter = latter.next
                former = former.next
            
            # Rotate the list
            newHead = former.next
            latter.next = head
            former.next = None
            
            return newHead