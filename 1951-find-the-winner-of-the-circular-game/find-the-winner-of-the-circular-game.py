class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        game = list(range(n))
        
        ptr = 0
        
        while len(game) > 1:
           ptr = (ptr + k - 1) % len(game)
           game.pop(ptr)
        
        return game[0] + 1