class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v = "".join(s.split()).lower()
        var = "".join(filter(str.isalnum, str(v)))
        if var[::-1] == var:
            return 1
        return 0