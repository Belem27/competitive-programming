# Problem: D - Heap Operations - https://codeforces.com/gym/535309/problem/D

from sys import stdin
from heapq import heapify, heappop, heappush

def input():
    return stdin.readline().strip()

t = int(input())
heap = []
heapify(heap)
ans = []

def insert(num):
    heappush(heap, num)
    ans.append(f"insert {num}")
    return

def getMin(num):
    while len(heap) >= 1 and heap[0] < num:
        remove()
    if heap and heap[0] > num:
        insert(num)
    if not heap:
        insert(num)
    ans.append(f"getMin {num}")
    return

def remove():
    if heap:
        heappop(heap)
        ans.append("removeMin")
    else:
        insert(0)
        remove()
    return


for _ in range(t):
    inputs = list(input().split())
    if len(inputs) > 1:
        func = inputs[0]
        num = int(inputs[1])
        if func == "insert":
            insert(num)
        else:
            getMin(num)
    else:
        remove()

print(len(ans))
for i in range(len(ans)):
    print(ans[i])