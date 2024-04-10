class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)
        print(piles)
        
        i = 1        
        coins = 0
        
        while i < len(piles) - (len(piles) //3):
            print(i)
            coins += piles[i]
            i += 2
            
        return coins
