"""
Given an array of integers, find if the array contains any duplicates. Your function 
should return true if any value appears at least twice in the array, and it should 
return false if every element is distinct.

URL: https://leetcode.com/problems/contains-duplicate/
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        elif len(nums) == 1:
            return False
        else:
            dup_dict = {}
            
            for entries in nums:
                if entries in dup_dict:
                    return True
                else:
                    dup_dict[entries] = 1
            return False