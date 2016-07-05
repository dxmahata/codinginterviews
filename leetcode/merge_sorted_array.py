"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) 
to hold additional elements from nums2. The number of elements initialized in 
nums1 and nums2 are m and n respectively.

URL: https://leetcode.com/problems/merge-sorted-array/
"""

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        last1 = m - 1
        last2 = n - 1
        last = m+n-1
        
        while (last1 >= 0 and last2 >=0):
            if nums1[last1] >= nums2[last2]:
                nums1[last] = nums1[last1]
                last1 -= 1
                last -= 1
            else:
                nums1[last] = nums2[last2]
                last2 -= 1
                last -= 1
                
        while(last2 >=0):
            nums1[last] = nums2[last2]
            last2 -= 1
            last -= 1