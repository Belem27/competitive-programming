# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        hm = {}

        for row in edges:
            for edge in row:
                hm[edge] = hm.get(edge, 0)+1

        return max(zip(hm.values(), hm.keys()))[1]