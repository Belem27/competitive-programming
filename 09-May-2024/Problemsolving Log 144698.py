# Problem: Problemsolving Log - https://codeforces.com/gym/522997/problem/A

def solved_problems(log):
    s = set(log)
    solved = 0
    for letter in s:
        if log.count(letter) >= ord(letter) - 64:
            solved += 1
    return solved

for _ in range(int(input())):
    n = int(input())
    log = list(input())
    print(solved_problems(log))