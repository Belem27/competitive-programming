# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(2,len(nums)):
            nums[i] = max(nums[:i-1]) + nums[i]
        print(nums)
        return max(nums)