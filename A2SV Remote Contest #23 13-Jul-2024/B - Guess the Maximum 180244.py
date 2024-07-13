# Problem: B - Guess the Maximum - https://codeforces.com/gym/535309/problem/B

for i in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	k = []
	for i in range(n-1):
		k.append(max(a[i],a[i+1]))
	print(min(k)-1)