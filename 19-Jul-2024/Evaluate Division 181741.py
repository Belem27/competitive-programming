# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a,b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q=deque()
            visited = set()
            q.append([src, 1])
            visited.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append([nei, w*weight])
            return -1
        return [bfs(q[0], q[1]) for q in queries]