class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = int(sqrt(c))

        while i <= j:
            sum_ = i**2 + j**2
            if sum_ == c:
                return True
            elif sum_ < c:
                i += 1
            else:
                j -= 1
        return False