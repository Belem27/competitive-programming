# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

n = int(input())
ans = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            ans += 1
print(ans//2)