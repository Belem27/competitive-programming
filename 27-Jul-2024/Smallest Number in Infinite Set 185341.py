# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet(object):

    def __init__(self):
        self.__n = 1
        self.__lookup = set()
        self.__min_heap = []

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.__min_heap:
            result = heapq.heappop(self.__min_heap)
            self.__lookup.remove(result)
            return result
        result = self.__n
        self.__n += 1
        return result

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num >= self.__n or num in self.__lookup:
            return
        self.__lookup.add(num)
        heapq.heappush(self.__min_heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)