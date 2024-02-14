class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        more = []
        pivot_arr = []
        result = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                pivot_arr.append(num)

        for num in less:
            result.append(num)
        for num in pivot_arr:
            result.append(num)
        for num in more:
            result.append(num)
        
        return result