# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += min(grid[i][j - 1] if j > 0 else float("inf"), grid[i - 1][j] if i > 0 else float("inf")) if i!=0 or j != 0 else 0
        return grid[-1][-1]