# Problem: B - New Year Transportation - https://codeforces.com/gym/532332/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))

c = 1

while c < t:
    c += a[c-1]

if t == c:
    print("YES")
else:
    print("NO")