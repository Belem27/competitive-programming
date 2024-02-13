class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        position = {num: i for i, num in enumerate(nums)}
        for i, j in operations:
            nums[position[i]] = j
            position[j] = position[i]
            del position[i]
        
        return nums
        
        return result