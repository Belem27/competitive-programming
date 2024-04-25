# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack_dict = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                stack_dict[stack.pop()] = num
            stack.append(num)

        while stack:
            stack_dict[stack.pop()] = -1
        
        ans = [stack_dict[num] for num in nums1]
        return ans

        