# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if char == "*" and len(stack) != 0:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)