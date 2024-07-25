# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet(object):

    def __init__(self):
        self.present = [True for _ in range(1001)]
        

    def popSmallest(self):
        """
        :rtype: int
        """
        for x in range(1, 1001):
            if self.present[x]:
                self.present[x] = False
                return x

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.present[num] = True
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)