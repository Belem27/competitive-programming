class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        expected = heights[:]
        expected.sort()

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count