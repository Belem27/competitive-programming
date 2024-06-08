# Problem: A - Magic Numbers - https://codeforces.com/gym/528793/problem/A

n = input()
a = n.count("144")
b = n.count("14")
c = n.count("1")
if len(n) - (a+b+c) == 0:
    print("YES")
else:
    print("NO")