class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_sum = 0

        for i in range(len(nums)//2):
            curr_sum = nums[i] + nums[~i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum