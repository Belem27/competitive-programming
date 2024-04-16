class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        max_length = 0
        
        for i in range(1, n - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left, right = i - 1, i + 1
                
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1
                
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                max_length = max(max_length, right - left + 1)
        
        return max_length
