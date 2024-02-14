class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive_arr = []
        negative_arr = []
        result = []

        for num in nums:
            if num > 0:
                positive_arr.append(num)
            elif num < 0:
                negative_arr.append(num)
        
        for i in range(len(zip(positive_arr, negative_arr))):
            result.append(positive_arr[i])
            result.append(negative_arr[i])
        
        return result