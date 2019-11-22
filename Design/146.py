# LRU Cache

# https://leetcode.com/problems/lru-cache/discuss/426763/Python-Faster-than-99.9-Simple-%2B-Explained
# run time: faster than 91.91%
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dic = {}
        
    def get(self, key: int) -> int:
        if key in self.dic:
            val = self.dic.pop(key)
            self.dic[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        self.dic[key] = value
        
        if len(self.dic) > self.size:
            self.dic.pop(next(iter(self.dic.keys()))) # get the first key and pop it


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)