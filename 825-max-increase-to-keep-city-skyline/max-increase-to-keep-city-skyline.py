class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum_ = 0
        cols = [max(i) for i in zip(*grid)]
        rows = [max(i) for i in grid]

        for i in range(len(grid)):
            for j in range(len(grid)):
                sum_ += min(cols[j], rows[i]) - grid[i][j]

        return sum_