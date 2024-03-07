class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0

        i, j = 0, len(height) - 1

        while i < j:
            l, h = j - i, 0

            if height[j] > height[i]:
                h =  height[i]
                i += 1
            else:
                h = height[j]
                j -= 1

            area = l * h

            max_area = max(max_area, area)
            
        return max_area
