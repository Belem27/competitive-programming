class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        
        peak = arr.index(max(arr))
        
        if peak == 0 or peak == n-1:
            return False
        
        for i in range(1, peak+1):
            if arr[i] <= arr[i-1]:
                return False
        
        for i in range(peak, n-1):
            if arr[i] <= arr[i+1]:
                return False
        
        return True

                