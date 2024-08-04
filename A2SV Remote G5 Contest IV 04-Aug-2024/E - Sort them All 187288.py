# Problem: E - Sort them All - https://codeforces.com/gym/507024/problem/E

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = []
 
    for _ in range(n):
        for i in range(n-1):
            if a[i] > a[i+1] or (a[i] == a[i+1] and b[i] > b[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                b[i], b[i+1] = b[i+1], b[i]
                ans.append((i+1, i+2))
 
    if sorted(b) == b:
        print(len(ans))
        for i in ans:
            print(*i)
    else:
        print(-1)