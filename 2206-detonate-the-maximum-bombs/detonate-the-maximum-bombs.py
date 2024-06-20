class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in xrange(len(bombs))]
        for i, (xi, yi, ri) in enumerate(bombs):
            for j, (xj, yj, _) in enumerate(bombs):
                if j == i:
                    continue
                if (xi-xj)**2+(yi-yj)**2 <= ri**2:
                    adj[i].append(j)
        result = 0
        for i in xrange(len(bombs)):
            stk = [i]
            lookup = {i}
            while stk:
                u = stk.pop()
                for v in adj[u]:
                    if v in lookup:
                        continue
                    lookup.add(v)
                    stk.append(v)
            result = max(result, len(lookup))
            if result == len(bombs):
                break
        return result