# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            graph[i+1].append(j+1)

ans = 0
for i in range(1, n+1):
    ans += len(graph[i])
print(ans//2)