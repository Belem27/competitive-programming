# Problem: A - Rudolph and Cut the Rope  - https://codeforces.com/gym/533316/problem/A

for _ in range(int(input())):
    n = int(input())
    res = 0
    for _ in range(n):
        a,b = map(int, input().split())
        if a > b:
            res += 1
    
    print(res)