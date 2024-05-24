# Problem: D - Team Composition: Programmers and Mathematicians - https://codeforces.com/gym/524150/problem/D

def max_teams(t, cases):
    res = []
    for case in cases:
        a, b = case
        res.append(min((a + b ) //4, min(a, b)))
    return res
t = int(input())
for ans in max_teams(t, [tuple(map(int, input().strip().split())) for _ in range(t)]):
    print(ans)