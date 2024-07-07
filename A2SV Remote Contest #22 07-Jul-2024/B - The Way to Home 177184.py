# Problem: B - The Way to Home - https://codeforces.com/gym/533316/problem/B

import sys

def soln(n, d, s):
    curr_pos = 0
    jumps = 0
    
    while curr_pos < n - 1:
        next_pos = curr_pos
        for i in range(1, d + 1):
            if curr_pos + i < n and s[curr_pos + i] == '1':
                next_pos = curr_pos + i
        
        if next_pos == curr_pos:
            return -1
        
        curr_pos = next_pos
        jumps += 1
        
    return jumps

input = sys.stdin.read
data = input().split()
n = int(data[0])
d = int(data[1])
s = data[2]

if __name__ == "__main__":
    print(soln(n, d, s))
