# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)

        def dfs(i, graph, visited):
            visited.add(i)
            for neighbor in graph[i]:
                if neighbor not in visited:
                    dfs(neighbor, graph, visited)
        
        visited = set()
        count = 0
        for i in range(1,n+1):
            if i not in visited:
                count += 1
                dfs(i, graph, visited)
            
        return count