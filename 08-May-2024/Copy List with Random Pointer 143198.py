# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        node_map = {}

        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copied_node = node_map[curr]
            if curr.next:
                copied_node.next = node_map[curr.next]
            if curr.random:
                copied_node.random = node_map[curr.random]
            curr = curr.next
        return node_map[head]
        