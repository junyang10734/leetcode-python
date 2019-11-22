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
            self.dic.pop(next(iter(self.dic.keys())))  # get the first key and pop it

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)
