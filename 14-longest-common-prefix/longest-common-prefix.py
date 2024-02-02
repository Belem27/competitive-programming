class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Iterate through characters in the first string
        for i, char in enumerate(strs[0]):
            # Check if the character matches in all strings
            for string in strs[1:]:
                # If the index is out of bounds or the character doesn't match, return the prefix
                if i >= len(string) or char != string[i]:
                    return strs[0][:i]

        # If all characters match, return the entire first string as the common prefix
        return strs[0]