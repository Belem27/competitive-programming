# Problem:  King Escape - https://codeforces.com/problemset/problem/1033/A

inp=int(input())
ax,ay=(map(int,input().split()))
bx,by=(map(int,input().split()))
cx,cy=(map(int,input().split()))
if (ax-cx)*(ax-bx)>0 and (ay-cy)*(ay-by)>0:
    print('YES')
else:
    print('NO')
