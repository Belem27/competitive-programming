# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, t = map(int, input().split())
a = list(map(int, input().split()))
i = 0
t -= 1 

while i < t:  
    i += a[i]  

print("YES" if i == t else "NO")
