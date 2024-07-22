# Problem: A - Hit the Lottery - https://codeforces.com/gym/536373/problem/A

def soln(n):
    bills_100 = n // 100
    n = n % 100
    bills_20 = n // 20
    n = n % 20
    bills_10 = n // 10
    n = n % 10
    bills_5 = n // 5
    n = n % 5
    bills_1 = n
    
    total_bills = bills_100 + bills_20 + bills_10 + bills_5 + bills_1
    return total_bills

n = int(input())
print(soln(n))