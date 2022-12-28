# 460. LFU Cache
# Hash Table / Doulby-Linked List


# https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    def __init__(self):
        self.dummy = Node()
        self.dummy.next = self.dummy.prev = self.dummy
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def appendNode(self, node):
        node.next = self.dummy.next
        node.prev = self.dummy
        node.next.prev = node
        self.dummy.next = node
        self.size += 1
        
    def popNode(self, node=None):
        if self.size == 0:
            return
        if not node:
            node = self.dummy.prev
        
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node
    
    
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.freq = collections.defaultdict(DLinkedList)
        self.minfreq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freq[self.minfreq].popNode()
                del self.cache[node.key]
                self.size -= 1
            
            node = Node(key, value)
            self.cache[key] = node
            self.freq[1].appendNode(node)
            self.minfreq = 1
            self.size += 1
    
    def update(self, node):
        freq = node.freq
        self.freq[freq].popNode(node)
        if self.minfreq == freq and self.freq[freq].getSize() == 0:
            self.minfreq += 1
        
        node.freq += 1
        self.freq[node.freq].appendNode(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)