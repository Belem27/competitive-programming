# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        result = total = sum(nums[:k])
        for i in xrange(k, len(nums)):
            total += nums[i] - nums[i-k]
            result = max(result, total)
        return float(result) / k