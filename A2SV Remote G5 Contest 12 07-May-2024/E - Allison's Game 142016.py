# Problem: E - Allison's Game - https://codeforces.com/gym/520098/problem/E

N = int(input())
heights = list(map(int, input().split()))

stack = []
max_area = 0

for i in range(N):
    while stack and heights[stack[-1]] >= heights[i]:
        height = heights[stack.pop()]
        width = i if not stack else i - stack[-1] - 1
        side = min(height, width)
        max_area = max(max_area, side)
    stack.append(i)

while stack:
    height = heights[stack.pop()]
    width = N if not stack else N - stack[-1] - 1
    side = min(height, width)
    max_area = max(max_area, side)

print(max_area)