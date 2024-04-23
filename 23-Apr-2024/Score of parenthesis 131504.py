# Problem: Score of parenthesis - https://leetcode.com/problems/score-of-parentheses/

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                score = stack.pop()
                if score == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * score
        return sum(stack)