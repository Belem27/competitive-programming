class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = [0] * len(nums)
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            running_sum[i] = current_sum
        
        return running_sum