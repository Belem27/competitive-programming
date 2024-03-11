class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()

        return next(num for num in nums if num in seen or seen.add(num))
        
