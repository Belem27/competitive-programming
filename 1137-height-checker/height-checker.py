class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0

        for i in range(len(heights)):
            if heights[i] != sorted(heights)[i]:
                count += 1

        return count