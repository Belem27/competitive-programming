class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def possible(piles, h, K):
            return sum((pile-1)//K+1 for pile in piles) <= h

        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right-left)//2
            if possible(piles, h, mid):
                right = mid-1
            else:
                left = mid+1
        return left