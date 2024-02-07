class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1_concat = "".join(word1)
        word2_concat = "".join(word2)

        if word1_concat == word2_concat:
            return True
        else:
            return False
        