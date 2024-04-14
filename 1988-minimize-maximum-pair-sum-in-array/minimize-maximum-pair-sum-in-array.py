class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_sum = 0
        n = len(nums)//2

        for i in range(n):
            curr_sum = nums[i] + nums[~i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum