# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder(object):

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.maxHeap, -1 * num)
        if self.maxHeap and self.minHeap and (-1 * self.maxHeap[0] )> self.minHeap[0]:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if len(self.maxHeap) > len(self.minHeap)+1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > len(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap)>len(self.minHeap):
            return -1 * self.maxHeap[0]
        elif len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        else:
            num1 = -1 * self.maxHeap[0]
            num2 = self.minHeap[0]
            return (num1 + num2) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()