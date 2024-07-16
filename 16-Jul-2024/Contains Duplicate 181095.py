# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = set()
        for num in nums:
            if num in dup:
                return True
            dup.add(num)
        return False