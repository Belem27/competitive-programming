class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort = sorted(nums)
        n = len(nums)
        result = []

        for i in range(n):
            idx = sort.index(nums[i])
            result.append(idx)

        return result