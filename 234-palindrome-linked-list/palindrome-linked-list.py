# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverseLinkedList(node):
            prev = None
            current = node
            
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            return prev
        
        def findMiddle(node):
            slow = node
            fast = node
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        middle = findMiddle(head)
        reversed_second_half = reverseLinkedList(middle)
        
        first_half = head
        second_half = reversed_second_half
        
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True