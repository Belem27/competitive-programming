class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(set(s)) == 1:
            return len(s)
        else:
            count = Counter(s)
            ans = 0
            odd = False
            for a in count:
                if count[a] % 2 == 0:
                    ans += count[a]
                else:
                    ans += (count[a] - 1)
                    odd = True
            if odd:
                ans += 1

            return ans