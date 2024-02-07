class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        if num%3==0:
            n=num//3
            result.append(n-1)
            result.append(n)
            result.append(n+1)
            return result
        else:
            return result