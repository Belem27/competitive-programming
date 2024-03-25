class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_map = {}
        
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
        
        palindrome_length = 0
        has_odd_freq = False
        
        for freq in freq_map.values():
            if freq % 2 == 0:
                palindrome_length += freq
            else:
                palindrome_length += freq - 1
                has_odd_freq = True
        
        if has_odd_freq:
            palindrome_length += 1
        
        return palindrome_length