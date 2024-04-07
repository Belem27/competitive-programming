class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def countStartEndVowel(words):
            n = len(words)
            count = [0] * (n + 1)

            for i in range(1, n + 1):
                word = words[i - 1]
                count[i] = count[i - 1] + (1 if word[0] in 'aeiou' and word[-1] in 'aeiou' else 0)

            return count

        counts = countStartEndVowel(words)
        ans = []

        for query in queries:
            left, right = query
            ans.append(counts[right + 1] - counts[left])

        return ans