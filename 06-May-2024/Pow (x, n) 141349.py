# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def helper(x, n):
            if n == 0: return 1
            if x == 0: return 0
            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))
        return 1/res if n <= 0 else res