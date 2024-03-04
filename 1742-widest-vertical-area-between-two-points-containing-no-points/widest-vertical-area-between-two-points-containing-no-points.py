class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        sol = 0
        ans = 0
        for i in range(1, len(points)):
            sol = points[i][0] - points[i-1][0]
            if ans < sol:
                ans = sol
        return ans