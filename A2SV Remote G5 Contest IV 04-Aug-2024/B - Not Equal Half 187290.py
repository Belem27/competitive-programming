# Problem: B - Not Equal Half - https://codeforces.com/gym/507024/problem/B

n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[:n] != a[n:]:
    print(*a)
else:
    print(-1)