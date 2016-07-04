"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to 
[5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways 
to solve this problem.
URL: https://leetcode.com/problems/rotate-array/
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2 or k == 0:
            pass
        else:
            if k >= n:
                k = k % n
            a = n - k
            self.reverse(nums, 0, a-1)
            self.reverse(nums, a, n-1)
            self.reverse(nums, 0, n-1)
        
    
    def reverse(self, nums, start, end):
        i = start
        j = end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
if __name__ == "__main__":
    soln = Solution()
    nums = [1,2,3,4,5,6,7]
    soln.rotate(nums, 3)
    print(nums)
    