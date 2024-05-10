# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        if target not in nums:
            return [-1,-1]

        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] != target:
                while nums[l] != target:
                    l += 1
            elif nums[r] != target:
                while nums[r] != target:
                    r -= 1
            else:
                return [l,r]
        return [l,r]