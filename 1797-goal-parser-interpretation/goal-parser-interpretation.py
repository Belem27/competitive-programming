class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = command.replace("()", "o")
        res = res.replace("(", "")
        res = res.replace(")", "")
        
        return res