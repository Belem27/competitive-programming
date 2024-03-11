class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the largest index k such that nums[k] < nums[k + 1]
        k = len(nums) - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        
        # If no such index exists, reverse the entire array and return
        if k == -1:
            nums.reverse()
            return nums
        
        # Step 2: Find the largest index l greater than k such that nums[k] < nums[l]
        l = len(nums) - 1
        while l > k and nums[l] <= nums[k]:
            l -= 1
        
        # Step 3: Swap the value of nums[k] with nums[l]
        nums[k], nums[l] = nums[l], nums[k]
        
        # Step 4: Reverse the elements from index k + 1 to the end of the array
        nums[k + 1:] = reversed(nums[k + 1:])
        
        return nums