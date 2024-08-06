class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        def dfs(i):
            if i >= n: return 1 if i == n else 0
            if i not in memo:
                memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)