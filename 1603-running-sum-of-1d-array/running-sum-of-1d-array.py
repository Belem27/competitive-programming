class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rs = [0] * len(nums)
        for i in range(len(nums)):
            rs[i] = sum(nums[:i + 1])

        return rs