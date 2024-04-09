class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        return sum(min(tickets[k] - (i > k), num) for i,num in enumerate(tickets))
