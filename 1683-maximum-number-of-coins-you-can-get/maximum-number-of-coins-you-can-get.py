class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)
        ans = 0

        for _ in range((len(piles)//3)):
            piles.pop(0)
            ans += piles.pop(0)
        
        return ans