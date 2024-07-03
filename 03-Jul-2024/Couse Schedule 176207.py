# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = collections.defaultdict(list)
        in_degree = collections.Counter()
        for u, v in prerequisites:
            in_degree[u] += 1
            adj[v].append(u)
        result = []
        q = [u for u in xrange(numCourses) if u not in in_degree]
        while q:
            new_q = []
            for u in q:
                result.append(u)
                for v in adj[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        new_q.append(v)
            q = new_q
        return len(result) == numCourses
