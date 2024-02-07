class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_consecutive_1 = 0
        count = 0
        
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_consecutive_1 = max(max_consecutive_1, count)
                count = 0
        max_consecutive_1 = max(max_consecutive_1, count)
        return max_consecutive_1


        