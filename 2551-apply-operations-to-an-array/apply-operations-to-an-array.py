class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and i < len(nums):
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        a = [0 for _ in range(nums.count(0))]
        x = [i for i in nums if i != 0]
        x.extend(a)
        return x