class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive_arr = [num for num in nums if num > 0]
        negative_arr = [num for num in nums if num < 0]
        result = [val for pair in zip(positive_arr[:len(nums)//2], negative_arr[:len(nums)//2]) for val in pair]
        
        return result