# Problem: C - Potions (Hard Version) - https://codeforces.com/gym/536373/problem/C

import heapq

def max_potions(n, potions):
    current_health = 0
    min_heap = []
    num_potions = 0

    for potion in potions:
        if current_health + potion >= 0:
            current_health += potion
            heapq.heappush(min_heap, potion)
            num_potions += 1
        elif min_heap and potion > min_heap[0]:
            current_health += potion - heapq.heappop(min_heap)
            heapq.heappush(min_heap, potion)
    
    return num_potions

# Reading input
n = int(input())
potions = list(map(int, input().split()))

# Getting the result
result = max_potions(n, potions)

# Printing the result
print(result)