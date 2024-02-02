class Solution(object):
    def smallestEvenMultiple(self, n):
        multiple = n

        while multiple % 2 != 0:
            multiple += n

        return multiple
        