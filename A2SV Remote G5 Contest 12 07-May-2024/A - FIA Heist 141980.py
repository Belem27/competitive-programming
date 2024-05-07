# Problem: A - FIA Heist - https://codeforces.com/gym/520098/problem/A

def decode_intercepted_string(s):
    stack = []
    for char in s:
        if char == '-' and stack and stack.pop() == "<":
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

intercepted_string = input().strip()

print(decode_intercepted_string(intercepted_string))