class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        return max(len(pos), len(neg))