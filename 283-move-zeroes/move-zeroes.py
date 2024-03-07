class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr = []
        while 0 in nums:
            nums.remove(0)
            arr.append(0)

        nums.extend(arr)