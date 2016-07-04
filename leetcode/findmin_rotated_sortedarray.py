"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None
        if nums[0] <= nums[len(nums)-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while (start <= end):
            mid = (start + end) // 2
            if mid <= len(nums) - 1 and nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            elif nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        return None
        