'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

URL: https://leetcode.com/problems/intersection-of-two-linked-lists/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None and headB == None:
            return None
        else:
            temp1 = headA
            temp2 = headB
            lengthA = 0
            lengthB = 0
            
            while temp1 != None:
                lengthA += 1
                temp1 = temp1.next
                
            while temp2 != None:
                lengthB += 1
                temp2 = temp2.next
                
            if lengthA >= lengthB:
                temp1 = headA
                temp2 = headB
                diff = lengthA-lengthB
            else:
                temp1 = headB
                temp2 = headA
                diff = lengthB - lengthA
                
            i = 0
            while i < diff:
                temp1 = temp1.next
                i += 1
            
            while temp1 != None and temp2 != None:
                if temp1 == temp2:
                    return temp1
                else:
                    temp1 = temp1.next
                    temp2 = temp2.next
