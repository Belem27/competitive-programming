class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_char_count = Counter(words[0])

        for word in words[1:]:
            common_char_count &= Counter(word)

        res = []

        for char, count in common_char_count.items():
            res.extend([char] * count)

        return res