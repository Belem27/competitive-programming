# Problem: C - Potions (Hard Version) - https://codeforces.com/gym/536373/problem/C

import heapq

n = int(input())
potions = list(map(int, input().split()))

heap = []
health = 0

for num in potions:
    health += num
    heapq.heappush(heap, num)
    if health < 0:
        health -= heapq.heappop(heap)

print(len(heap))