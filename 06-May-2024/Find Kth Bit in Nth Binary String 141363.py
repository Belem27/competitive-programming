# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        flip, l = 0, 2**n-1
        while k > 1:
            if k == l//2+1:
                flip ^= 1
                break
            if k > l//2:
                k = l+1-k
                flip ^= 1
            l //= 2
        return str(flip)