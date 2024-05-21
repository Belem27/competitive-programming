# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        def find_peak():
            left, right = 0, mountain_arr.length() - 1
            while left < right:
                mid = (left + right) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search(left, right, target, asc=True):
            while left <= right:
                mid = (left + right) // 2
                value = mountain_arr.get(mid)
                if value == target:
                    return mid
                if (value < target and asc) or (value > target and not asc):
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        n = mountain_arr.length()
        peak = find_peak()

        # Search in the ascending part
        index = binary_search(0, peak, target, asc=True)
        if index != -1:
            return index

        # Search in the descending part
        return binary_search(peak + 1, n - 1, target, asc=False)