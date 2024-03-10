class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        target = 0
        for idx, val in hashmap.items():
            for i in range(val):
                nums[target] = idx
                target += 1