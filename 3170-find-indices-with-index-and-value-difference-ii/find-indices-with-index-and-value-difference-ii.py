class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        n = len(nums)
        mini = maxi = 0
        for i in range(indexDifference, n):
            if nums[i - indexDifference] < nums[mini]: mini = i - indexDifference
            if nums[i - indexDifference] > nums[maxi]: maxi = i - indexDifference
            if nums[i] - nums[mini] >= valueDifference: return [mini, i]
            if nums[maxi] - nums[i] >= valueDifference: return [maxi, i]
            
        return [-1, -1]