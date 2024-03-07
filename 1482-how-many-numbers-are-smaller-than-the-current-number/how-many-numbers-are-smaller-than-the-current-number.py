class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []

        for i in range(n):
            count = 0
            for j in range(n):
                if j != i and nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result