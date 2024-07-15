# Problem: C - The Lakes - https://codeforces.com/gym/535309/problem/C

def bfs(x,y):
	s = a[x][y]
	a[x][y] = 0
	q = [(x,y)]
	while q:
		x,y = q.pop()
		for nx, ny in (x,y-1),(x-1,y),(x,y+1),(x+1,y):
			if 0 <=nx < b and 0<=ny < c and a[nx][ny]:
				s+=a[nx][ny]
				a[nx][ny] = 0
				q.append((nx,ny))
	return s
for _ in range(int(input())):
	b,c = map(int, input().split())
	a = [list(map(int, input().split())) for i in range(b)]
	ans = 0
	for i in range(b):
		for j in range(c):
			if a[i][j]:
				ans = max(ans,bfs(i,j))
	print(ans)	  	   	 	 	    	 	