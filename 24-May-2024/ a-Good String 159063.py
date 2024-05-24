# Problem:  a-Good String - https://codeforces.com/gym/522997/problem/C

t = int(input())
 
def solve(x,z):
	if len(x)==0:
		return 0
	if len(x)==1:
		return int(x!=z)
	m = len(x)//2
	L = x[:m]
	R = x[m:]
	a = (m-L.count(z))+solve(R,chr(ord(z)+1))
	b = (m-R.count(z))+solve(L,chr(ord(z)+1))
	return min(a,b)
 
while t:
	n = int(input())
	S = input()
	print(solve(S,"a"))
	t = t - 1