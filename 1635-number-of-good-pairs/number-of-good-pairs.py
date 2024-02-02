class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_of_good_pair = 0
        num_count = {}
        for num in nums:
            if num in num_count:
                num_of_good_pair += num_count[num]
                num_count[num] += 1
            else:
                num_count[num] = 1

        return num_of_good_pair
