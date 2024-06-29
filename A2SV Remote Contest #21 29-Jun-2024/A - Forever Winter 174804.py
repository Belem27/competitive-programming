# Problem: A - Forever Winter - https://codeforces.com/gym/532332/problem/A

from collections import Counter


def solve():
    n, m = map(int, input().split())

    g = [0 for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        g[u - 1] += 1
        g[v - 1] += 1

    cnt = Counter(g)
    print(n - cnt[1] - 1, cnt[1]//(n - cnt[1] - 1))


for i in range(int(input())):
    solve()