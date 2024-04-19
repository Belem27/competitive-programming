# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], []
    
        # Push digits of l1 onto stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        # Push digits of l2 onto stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        result = None
        
        # Pop digits from both stacks and add them together
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            
            # Construct a new node with the sum % 10
            new_node = ListNode(total % 10)
            new_node.next = result
            result = new_node
        
        return result

    # Helper function to reverse a linked list
    def reverseLinkedList(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev