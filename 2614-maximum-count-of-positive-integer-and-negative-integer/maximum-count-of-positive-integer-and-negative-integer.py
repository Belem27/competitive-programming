class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(len([num for num in nums if num > 0]), len([num for num in nums if num < 0]))