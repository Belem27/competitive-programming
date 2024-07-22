# Problem: B - Remove Smallest - https://codeforces.com/gym/536373/problem/B

def soln(n, a):

    a.sort()
    possible = True
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            possible = False
            break

    
    return "YES" if possible else "NO"

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(soln(n, a))
