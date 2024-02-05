class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                # Handle '10#' to '26#'
                char_code = int(s[i:i + 2])
                result += chr(ord('a') + char_code - 1)
                i += 3
            else:
                # Handle '1' to '9'
                char_code = int(s[i])
                result += chr(ord('a') + char_code - 1)
                i += 1

        return result