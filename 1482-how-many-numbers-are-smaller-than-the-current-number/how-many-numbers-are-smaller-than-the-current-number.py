class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums, reverse=True) # [8, 3, 2, 2, 1]
        smaller_count = {}
        for i in range(len(sorted_nums) - 1):
            curr_num = sorted_nums[i]
            next_num = sorted_nums[i + 1]
            if next_num < curr_num:
                remaining_values = len(sorted_nums) - (i + 1)
                smaller_count[curr_num] = remaining_values
            
        smaller_count[sorted_nums[-1]] = 0

        output = []
        for num in nums:
            output.append(smaller_count[num])

        return output