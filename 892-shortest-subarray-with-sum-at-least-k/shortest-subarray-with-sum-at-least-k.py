class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        dq = deque()
        min_length = float('inf')
        
        for i in range(n + 1):
            while dq and prefix_sums[i] - prefix_sums[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            
            while dq and prefix_sums[i] <= prefix_sums[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return min_length if min_length != float('inf') else -1