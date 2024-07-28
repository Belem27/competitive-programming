# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lookup = {c: i for i, c in enumerate(s)}
        first, last = 0, 0
        result = []
        for i, c in enumerate(s):
            last = max(last, lookup[c])
            if i == last:
                result.append(i-first+1)
                first = i+1
        return result