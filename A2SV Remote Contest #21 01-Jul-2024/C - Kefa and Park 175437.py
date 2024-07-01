# Problem: C - Kefa and Park - https://codeforces.com/gym/532332/problem/C

from collections import defaultdict, deque

n,m = map(int, input().split())
a = list(map(int, input().split()))
g = defaultdict(list)
for i in range(n-1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

q = deque()
q.append((1,0))
visited = set()
ans = 0

while q:
    for i in range(len(q)):
        node, cnt = q.popleft()
        if node in visited:
            continue

        visited.add(node)
        if a[node-1]:
            cnt += 1
        else:
            cnt = 0
        
        if cnt > m:
            continue
        c = 0
        for i in g[node]:
            if i not in visited:
                c += 1
                q.append((i,cnt))
        if c == 0:
            ans += 1
print(ans)