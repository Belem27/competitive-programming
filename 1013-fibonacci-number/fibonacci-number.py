class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in xrange(n):
            prev, current = current, prev + current,
        return prev