class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def lcp(s1, s2):
            n = min(len(s1), len(s2))
            cp = ""
            for i in range(n):
                if s1[i] != s2[i]:
                    return cp
                cp += s1[i]
            
            return cp

        if len(strs) == 1:
            return strs[0]
        elif len(strs) < 1:
            return ""

        cp = lcp(strs[0], strs[1])
        for i in range(2, len(strs)):
            cp = lcp(cp, strs[i])
        
        return cp
        