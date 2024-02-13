class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        lost = defaultdict(int)
        
        for m in matches:
            lost[m[0]] += 0
            lost[m[1]] += 1
        
        no_losses = sorted([k for k, l in lost.items() if l == 0])
        one_loss = sorted([k for k, l in lost.items() if l == 1])
        return [no_losses, one_loss]