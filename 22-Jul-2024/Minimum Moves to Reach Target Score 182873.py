# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        result = 0
        while target > 1 and maxDoubles:
            result += 1+target%2
            target //= 2
            maxDoubles -= 1
        return result+(target-1)