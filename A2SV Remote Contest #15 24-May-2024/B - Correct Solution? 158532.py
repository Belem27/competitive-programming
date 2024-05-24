# Problem: B - Correct Solution? - https://codeforces.com/gym/524150/problem/B

alice = sorted(input())
bob = list(input())
i = 0
n = len(alice)-1
while i < n and alice[i] == "0":
    i += 1
alice[0], alice[i] = alice[i], alice[0]
if alice == bob:
    print("OK")
else:
    print("WRONG_ANSWER")
