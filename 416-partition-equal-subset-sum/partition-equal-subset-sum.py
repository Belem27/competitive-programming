class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sm, n = sum(nums), len(nums)
        if sm % 2:
            return False
        sm //= 2
        dp = [False] * (sm + 1)
        dp[0] = True
        for num in nums:
            for j in range(num, sm + 1)[::-1]:
                dp[j] = dp[j] or dp[j - num]
        return dp[-1]