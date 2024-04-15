class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = []

        if num > 0:
            num = sorted([int(n) for n in str(num)])
            i = 1
            while num[0] == 0:
                num[0], num[i] = num[i], num[0]
                i += 1

            for n in num:
                ans.append(n)

        elif num < 0:
            nl = str(num)
            num = [int(n) for n in str(nl[1:])]
            num.sort(reverse=True)
            for n in num:
                ans.append(n)
            ans.insert(0, "-")
        else:
            return num

        return int("".join(map(str, ans)))