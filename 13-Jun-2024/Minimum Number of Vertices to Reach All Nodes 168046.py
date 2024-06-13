# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        in_degrees = set()
        for i,j in edges:
            in_degrees.add(j)

        out_degrees = []
        for i in range(n):
            if i not in in_degrees:
                out_degrees.append(i)

        return out_degrees