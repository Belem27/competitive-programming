class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        running_sum = [0] * n  
        current_sum = 0  
        
        for i in range(n):
            current_sum += nums[i]
            running_sum[i] = current_sum
        
        return running_sum
