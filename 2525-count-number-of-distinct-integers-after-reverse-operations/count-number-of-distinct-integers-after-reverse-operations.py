class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reverse(n):
            result = 0
            while n:
                result = result*10 + n % 10
                n //= 10
            return result

        return len({y for x in nums for y in (x, reverse(x))})