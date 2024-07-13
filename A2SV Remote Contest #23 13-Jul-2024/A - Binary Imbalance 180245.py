# Problem: A - Binary Imbalance - https://codeforces.com/gym/535309/problem/A

t = int(input().strip())
cases = []
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    cases.append((n, s))
    results = []
    for case in cases:
        n = case[0]
        s = case[1]
        
        count_0 = s.count('0')
        count_1 = s.count('1')
        
        if count_0 > count_1:
            results.append("YES")
        else:
            can_insert_zero = False
            for i in range(n - 1):
                if s[i] != s[i + 1]:
                    can_insert_zero = True
                    break
            if can_insert_zero:
                results.append("YES")
            else:
                results.append("NO")
                
for res in results:
    print(res)