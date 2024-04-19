# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        
        # Find the meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # Check if there's no cycle
        if not fast or not fast.next:
            return None
        
        # Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow