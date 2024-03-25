class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = sum(map(lambda x: x & 1, collections.Counter(s).values()))
        return len(s) - odd + int(odd > 0)