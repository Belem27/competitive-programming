# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_to_front(self, node):
        # Remove the node from its current position
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # Move the node to the front of the list
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.move_to_front(node)
        return node.value
    
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used node
                lru_node = self.tail.prev
                del self.cache[lru_node.key]
                lru_node.prev.next = self.tail
                self.tail.prev = lru_node.prev
            
            # Add the new node to the front of the list
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node
