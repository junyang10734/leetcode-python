# 677. Map Sum Pairs
# Hash Table

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.score = collections.defaultdict(int)
        self.d = {}
        
    def insert(self, key: str, val: int) -> None:
        diff = val - self.d.get(key, 0)
        self.d[key] = val

        tmp = ''
        for i in range(len(key)):
            tmp += key[i]
            self.score[tmp] += diff   

    def sum(self, prefix: str) -> int:
        return self.score.get(prefix, 0)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)