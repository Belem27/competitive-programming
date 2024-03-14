class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(height != expected for height, expected in zip(heights, sorted(heights)))