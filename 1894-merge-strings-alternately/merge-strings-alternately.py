class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        l1, l2 = len(word1), len(word2)
        diff = l1 - l2
        i, j = 0, 0

        while i < l1 and j < l2:
            result.append(word1[i])
            result.append(word2[j])

            i += 1
            j += 1
        
        result.append(word1[i:])
        result.append(word2[i:])

        return ''.join(result)


        