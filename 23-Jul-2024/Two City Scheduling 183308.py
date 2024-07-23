# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        diffs = []
        res = 0

        for a,b in costs:
            diffs.append([b-a, a, b])
        
        diffs.sort()
        for i in range(len(diffs)):
            if i < len(diffs)//2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]

        return res