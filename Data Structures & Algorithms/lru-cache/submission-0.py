class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node_prev = node.prev
            node_next = node.next
            node_prev.next = node_next
            node_next.prev = node_prev
            last = self.right.prev
            last.next = node
            node.prev = last
            node.next = self.right
            self.right.prev = node
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node_prev = node.prev
            node_next = node.next
            node_prev.next = node_next
            node_next.prev = node_prev
            last = self.right.prev
            last.next = node
            node.prev = last
            node.next = self.right
            self.right.prev = node
            node.val = value
        else:
            if len(self.cache) >= self.capacity:
                victim = self.left.next
                start = victim.next
                self.left.next = start
                start.prev = self.left
                del self.cache[victim.key]
            
            last = self.right.prev
            new_node = Node(key, value)
            last.next = new_node
            new_node.prev = last
            new_node.next = self.right
            self.right.prev = new_node
            self.cache[key] = new_node


        
