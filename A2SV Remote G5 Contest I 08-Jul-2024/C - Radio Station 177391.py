# Problem: C - Radio Station - https://codeforces.com/gym/500425/problem/C

n, m = map(int, input().split())
q = {}
for _ in range(n):
    name, server = input().split()
    q[server] = name

for _ in range(m):
    command, server = input().split()
    ip = server[:-1]
    if ip in q:
        print(f"{command} {server} #{q[ip]}")