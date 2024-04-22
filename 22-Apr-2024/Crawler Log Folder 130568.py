# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []

        for operation in logs:
            if operation == "../" and stack:
                stack.pop()
            elif operation != "./" and operation != "../":
                stack.append(operation)
        
        print(stack)
        return len(stack)