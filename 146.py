# 146. LRU Cache

# OrderedDict
class LRUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.d:
            v = self.d[key]
            del self.d[key]
            self.d[key] = v
            return v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            self.d[key] = value
        else:
            if self.capacity == 0:
                self.d.popitem(last=False)
                self.d[key] = value
            else:
                self.d[key] = value
                self.capacity -= 1


# https://leetcode.com/problems/lru-cache/solution/
# Hashmap + DoubleLinkedList
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if not node:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.add_node(newNode)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self.move_to_head(node)

    
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def remove_node(self, node):
        prev = node.prev
        net = node.next
        prev.next = net
        net.prev = prev
    
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)
        
    def pop_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)