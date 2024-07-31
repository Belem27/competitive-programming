# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        heap = []

        for num, freq in count.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        
        res = []
        while heap:
            res.append(heappop(heap)[1])

        return res

        return res