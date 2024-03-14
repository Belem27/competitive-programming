# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n

        while l <= r:
            if guess((l + r) // 2) == 0:
                return (l + r) // 2
            elif guess((l + r) // 2) == 1:
                l = ((l + r) // 2) + 1
            else:
                r = ((l + r) // 2) - 1

        return ((l + r) // 2) 