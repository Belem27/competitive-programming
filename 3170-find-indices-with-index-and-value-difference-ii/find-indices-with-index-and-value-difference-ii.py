class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        n = len(nums)
        max_i = min_i = 0
        for i in xrange(n - indexDifference):
            if nums[i] > nums[max_i]:
                max_i = i
            elif nums[i] < nums[min_i]:
                min_i = i

            if nums[max_i] - nums[i + indexDifference] >= valueDifference:
                return [max_i, i + indexDifference]
            if nums[i + indexDifference] - nums[min_i] >= valueDifference:
                return [min_i, i + indexDifference]

        return [-1, -1]