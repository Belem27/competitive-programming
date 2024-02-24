class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_cat = str(int("".join(map(str, digits))) + 1)

        return list(map(int, digit_cat))