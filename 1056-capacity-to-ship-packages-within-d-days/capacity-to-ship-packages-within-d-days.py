class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def possible(weights, days, mid):
            result, curr = 1, 0
            for w in weights:
                if curr+w > mid:
                    result += 1
                    curr = 0
                curr += w
            return result <= days
    
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + (right-left)//2
            if possible(weights, days, mid):
                right = mid-1
            else:
                left = mid+1
        return left