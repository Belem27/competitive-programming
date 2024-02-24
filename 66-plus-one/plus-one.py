class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_cat = "".join([str(digit) for digit in digits])

        digit_plus_one = int(digit_cat) + 1

        return list(map(int, str(digit_plus_one)))