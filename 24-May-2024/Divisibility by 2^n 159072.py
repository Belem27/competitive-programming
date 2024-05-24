# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

t=int(input())
while t:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    s=0
    for x in range(n):
        y=a[x]
        while y%2==0:
            s+=1
            y//=2
        k=0
        y=x+1
        while y%2==0 and y:
            k+=1
            y//=2
        b.append(k)
    b.sort(reverse=True)
    javob=0
    for x in range(n):
        if s>=n:
            print(x)
            break
        s+=b[x]
    else:
        print(-1)