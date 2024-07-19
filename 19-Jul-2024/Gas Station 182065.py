# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas):
            return -1

        start = 0
        gas_lvl = 0

        for i in range(len(gas)):
            gas_lvl += gas[i] - cost[i]
            if gas_lvl < 0:
                start = i + 1
                gas_lvl = 0

        return start