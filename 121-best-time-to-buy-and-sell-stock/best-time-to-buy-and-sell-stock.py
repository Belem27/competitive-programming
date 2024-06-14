class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]
        for p in prices:
            buy = min(buy, p)
            profit = max(profit, p-buy)
        return profit