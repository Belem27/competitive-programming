# Problem: A - Forever Winter - https://codeforces.com/gym/532332/problem/A

for i in range(int(input())):
    n, m = map(int, input().split())
    g = [[] for j in range(n)]
    for j in range(m):
        v, u = map(int, input().split())
        g[v-1].append(u-1)
        g[u-1].append(v-1)
    q = {}
    for j in range(n):
        q[len(g[j])] = q.get(len(g[j]), 0) + 1
    z = q[1]
    x = n-z-1
    y = z//x
    print(x, y)