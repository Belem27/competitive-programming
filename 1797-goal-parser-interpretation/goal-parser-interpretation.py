class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = command.replace("()", "o").encode("ascii", "ignore")
        ans = ""
        for c in res:
            if ord(c) in range(45, 91) or ord(c) in range(97, 123):
                ans += c
        return ans