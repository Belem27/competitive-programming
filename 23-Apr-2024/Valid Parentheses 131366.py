# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {")":"(","}":"{","]":"["}

        for bracket in s:
            if bracket in bracket_map.values():
                stack.append(bracket)
            elif bracket in bracket_map:
                if not stack or stack.pop() != bracket_map[bracket]:
                    return False
        return not stack