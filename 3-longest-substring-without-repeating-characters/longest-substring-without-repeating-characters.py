class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0:
            return 0
        i, j, max_substr = 0, 0, 0
        stack = set()

        while i < len(s):
            while s[i] in stack:
                stack.remove(s[j])
                j += 1
            stack.add(s[i])
            max_substr = max(max_substr, abs(i - j + 1))
            i += 1

        return max_substr
