# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        
        prev_row = [1]  # Initialize the first row
        
        for i in range(1, rowIndex + 1):
            curr_row = [1] * (i + 1)  # Initialize the current row with 1s
            
            # Calculate the values for the current row (excluding the first and last elements)
            for j in range(1, i):
                curr_row[j] = prev_row[j - 1] + prev_row[j]
            
            prev_row = curr_row  # Update the previous row
            
        return prev_row