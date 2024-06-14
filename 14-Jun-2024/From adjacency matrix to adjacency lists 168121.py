# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for i in range(n):
    row = list(map(int, input().split()))
    
    for j in range(len(row)):
        graph[i].append(row[j])

for i in range(n):
    ans = []
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            ans.append(j+1)
    print(len(ans), *ans)
               
#print (graph)
