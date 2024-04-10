# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def reverse(l, begin, end):
            for i in xrange((end-begin) // 2):
                l[begin+i], l[end-1-i] = l[end-1-i], l[begin+i]

        result = []
        for n in reversed(xrange(1, len(arr)+1)):
            i = arr.index(n)
            reverse(arr, 0, i+1)
            result.append(i+1)
            reverse(arr, 0, n)
            result.append(n)
        return result