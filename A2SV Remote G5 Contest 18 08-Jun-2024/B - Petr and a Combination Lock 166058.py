# Problem: B - Petr and a Combination Lock - https://codeforces.com/gym/528793/problem/B

sums = {0}
for _ in range(int(input())):
    a = int(input())
    sums = set((a + x) % 360 for x in sums) | set((a - x) % 360 for x in sums)
 
print("YES" if 0 in sums else "NO")