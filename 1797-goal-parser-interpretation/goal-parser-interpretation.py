class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = command.replace("()", "o")

        return "".join(list([val for val in res if val.isalpha()]))