"""
Given an array of n integers nums and a target, find the number of index triplets 
i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]

URL: https://leetcode.com/problems/3sum-smaller/
"""
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 2 or len(nums) == 1:
            return len([])
        else:
            triplet_list = []
            sorted_nums = sorted(nums)
            for i in range(0, len(nums) - 2):
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    curr_sum = sorted_nums[i] + sorted_nums[start] + sorted_nums[end]
                    if curr_sum == target:
                        end -= 1
                    elif curr_sum < target:
                        triplet = (sorted_nums[i], sorted_nums[start], sorted_nums[end])
                        triplet_list.append(triplet)
                        start += 1
                    elif curr_sum > target:
                        end -= 1
            print(triplet_list)          
            #return len([list(entries) for entries in set(triplet_list)])
            return len(triplet_list)

if __name__ == "__main__":
    soln = Solution()
    print(soln.threeSumSmaller([3,1,0,-2], 4))