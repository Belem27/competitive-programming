# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0]*n
        adj = collections.defaultdict(set)
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            adj[a].add(b)
            adj[b].add(a)
        ans = 0
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                ans = max(ans, degree[i]+degree[j]-int(i in adj and j in adj[i]))
        return ans