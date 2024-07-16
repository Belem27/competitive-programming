# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = 0
        for i in range(len(nums)):
            if i > goal:
                break
            goal = max(goal, i + nums[i])
        return goal >= len(nums)-1