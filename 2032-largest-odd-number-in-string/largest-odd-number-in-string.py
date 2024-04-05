class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in reversed(xrange(len(num))):
            if int(num[i]) % 2 == 1:
                return num[:i + 1] 

        return ""