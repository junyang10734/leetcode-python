# 706. Design HashMap

# https://blog.csdn.net/fuxuemingzhu/article/details/81017297

# 一维数组
# runtime: faster than 32.42%
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.h[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.h[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.h[key] = -1


# 二维数组
# runtime: faster than 24.14%
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bitmap = [[-1] * 1000 for _ in range(1001)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        row, col = key // 1000, key % 1000
        self.bitmap[row][col] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        row, col = key // 1000, key % 1000
        return self.bitmap[row][col]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        row, col = key // 1000, key % 1000
        self.bitmap[row][col] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)