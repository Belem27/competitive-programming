# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        min_ = nums[0]
        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and num > stack[-1][1]:
                return True
            else:
                stack.append([num, min_])
                min_ = min(min_, num)
        return False