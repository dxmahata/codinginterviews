'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in 
the list, only nodes itself can be changed.

URL: https://leetcode.com/problems/swap-nodes-in-pairs/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        else:
            temp = head
            
            while temp != None and temp.next != None:
                self.swapData(temp, temp.next)
                temp = temp.next.next
                
            return head
                
    def swapData(self,node1,node2):
        tempNode = node1.val
        node1.val = node2.val
        node2.val = tempNode
