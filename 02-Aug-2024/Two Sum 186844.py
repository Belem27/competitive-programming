# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hm:
                return [hm[diff], i]
            hm[v] = i      
        return None
                