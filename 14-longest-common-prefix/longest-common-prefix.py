class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def LCP(s1, s2):
            n = min(len(s1), len(s2))
            common_prefix = ""
            for i in range(n):
                if s1[i] != s2[i]:
                    break
                common_prefix += s1[i]
            return common_prefix
        if len(strs) < 1:
            return ""
        elif len(strs) == 1:
            return strs[0]

        lcp = LCP(strs[0], strs[1])
        for i in range(2, len(strs)):
            lcp = LCP(lcp, strs[i])
        
        return lcp