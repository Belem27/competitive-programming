class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        def is_palindrome(s):
            return s == s[::-1]

        def check_condition(a, b):
            l, r = 0, len(a) - 1
            while l < r and a[l] == b[r]:
                l += 1
                r -= 1
            
            return is_palindrome(a[l:r + 1]) or is_palindrome(b[l:r + 1])

        return check_condition(a, b) or check_condition(b, a)