class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)
        ans = 0

        for i in range((len(piles)//3)):
            ans += piles[(i*2)+1]
        
        return ans