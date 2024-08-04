# Problem: C - Kenenisa's Dilemma - https://codeforces.com/gym/507024/problem/C

n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(arr)

if sort_arr == arr:
    print(0)
else:
    count = 0
    swaps = []
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            count += 1
            swaps.append(str(i) + " " + str(min_index))
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    print(count)
    print('\n'.join(swaps))
        