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
                if edge in hm:
                    hm[edge] += 1
                else:
                    hm[edge] = 1
        
        v = list(hm.values())
        k = list(hm.keys())

        return (k[v.index(max(v))])