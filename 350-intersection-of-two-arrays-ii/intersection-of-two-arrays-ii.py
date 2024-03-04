class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap = Counter(nums1)
        result = []

        for num in nums2:
            if num in hashmap and hashmap[num] > 0:
                result.append(num)
                hashmap[num] -= 1
        
        return result