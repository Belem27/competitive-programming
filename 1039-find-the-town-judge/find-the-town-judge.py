class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        degrees = [0]*n
        for i, j in trust:
            degrees[i-1] -= 1
            degrees[j-1] += 1
        for i in xrange(len(degrees)):
            if degrees[i] == n-1:
                return i+1
        return -1