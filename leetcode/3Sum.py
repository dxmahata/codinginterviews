"""Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

URL: https://leetcode.com/problems/3sum/
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums) == 2 or len(nums) == 1:
            return []
        else:
            sum_zero_list = []
            sorted_nums = sorted(nums)
            for i in range(0, len(nums) - 2):
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    curr_sum = sorted_nums[i] + sorted_nums[start] + sorted_nums[end]
                    if curr_sum == 0:
                        zero_triplet = (sorted_nums[i], sorted_nums[start], sorted_nums[end])
                        sum_zero_list.append(zero_triplet)
                        start += 1
                        end -= 1
                    elif curr_sum < 0:
                        start += 1
                    elif curr_sum > 0:
                        end -= 1
                        
            return [list(entries) for entries in set(sum_zero_list)]
                        
if __name__ == "__main__":
    soln = Solution()
    print(soln.threeSum([-1, 0, 1, 2, -1, -4]))