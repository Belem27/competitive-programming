# Problem: c - Reposts - https://codeforces.com/gym/533316/problem/c

import sys
input = sys.stdin.read

def soln(reposts):
    repost_chain = {}
    repost_chain["polycarp"] = 1

    for repost in reposts:
        name1, _, name2 = repost.lower().split()
        repost_chain[name1] = repost_chain[name2] + 1
    
    return max(repost_chain.values())

data = input().splitlines()
n = int(data[0])
reposts = data[1:]

if __name__ == "__main__":
    print(soln(reposts))
