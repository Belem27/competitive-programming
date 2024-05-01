# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
    
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                encoded_str = ''
                while stack[-1] != '[':
                    encoded_str = stack.pop() + encoded_str
                
                stack.pop()
                
                num_str = ''
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                
                k = int(num_str)
                decoded_str = k * encoded_str
                stack.extend(decoded_str)
        
        return ''.join(stack)
