# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
            
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        k = k % length
        
        if k == 0:
            return head
        
        current.next = head
        
        for _ in range(length - k):
            current = current.next
        
        new_head = current.next
        current.next = None
        
        return new_head     