# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

from collections import defaultdict
n = int(input())
graph = defaultdict(list)

for _ in range(int(input())):
    operations = list(map(int, input().split()))
    if operations[0] == 1:
        u,v = operations[1], operations[2]
        graph[u].append(v)
        graph[v].append(u)
    elif operations[0] == 2:
        u = int(operations[1])
        if u in graph:
            print(" ".join(map(str, graph[u])))