class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        fib_num = [0] * (n + 1)
        fib_num[1] = 1

        for i in range(2, n + 1):
            fib_num[i] = fib_num[i - 1] + fib_num[i - 2]
        
        return fib_num[n]