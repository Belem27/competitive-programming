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
            mid =  (l + r) // 2
            check = guess(mid)
            if check == 0:
                return mid
            elif check == 1:
                l = mid + 1
            else:
                r = mid - 1

        return mid 