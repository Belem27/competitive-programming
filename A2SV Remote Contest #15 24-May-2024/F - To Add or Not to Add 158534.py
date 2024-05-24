# Problem: F - To Add or Not to Add - https://codeforces.com/gym/524150/problem/F

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
l, r = 0, 1
max_c = 1
curr_num = arr[0]
curr_sum = arr[0]
while r < n:
    curr_sum += arr[r]
    while (arr[r] * (r - l + 1)) - curr_sum > k:
        curr_sum -= arr[l]
        l += 1 
    curr_size = r - l + 1
    if curr_size > max_c:
        max_c = curr_size
        curr_num = arr[r]
    r += 1
print(max_c, curr_num)