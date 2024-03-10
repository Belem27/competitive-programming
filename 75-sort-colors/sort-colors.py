class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = [], [], []

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(0)
            
            if nums[i] == 1:
                ones.append(1)

            if nums[i] == 2:
                twos.append(2)

        nums[:] = []

        nums.extend(zeros)
        nums.extend(ones)
        nums.extend(twos)