# 705. Design HashSet
# Design

# https://blog.csdn.net/fuxuemingzhu/article/details/81016992
# Array
# runtime: faster than 28.97%
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [False]*1000001

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.set[key]


# 二维数组
# runtime: faster than 73.49%
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.set = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        hashKey = self.hash(key)
        hashPos = self.pos(key)
        if not self.set[hashKey]:
            self.set[hashKey] = [0] * self.itemsPerBucket
        self.set[hashKey][hashPos] = 1

    def remove(self, key: int) -> None:
        hashKey = self.hash(key)
        hashPos = self.pos(key)
        if self.set[hashKey]:
            self.set[hashKey][hashPos] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashKey = self.hash(key)
        hashPos = self.pos(key)
        return self.set[hashKey] != [] and self.set[hashKey][hashPos] == 1
    
    def hash(self, key: int) -> int:
        return key // self.buckets
    
    def pos(self, key: int) -> int:
        return key % self.buckets



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)