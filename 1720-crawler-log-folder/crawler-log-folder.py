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
                stack.append(1)
        
        return len(stack)