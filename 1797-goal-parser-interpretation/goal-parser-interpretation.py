class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command = command.replace("()", "o")
        ans = ""
        for c in command:
            if ord(c) in range(45, 91) or ord(c) in range(97, 123):
                ans += c
        return ans