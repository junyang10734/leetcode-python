# 981. Time Based Key-Value Store

# hash / binary search
# https://leetcode.com/problems/time-based-key-value-store/solution/
# running time: faster than 66.60%
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        a = self.d[key]
        if len(a) == 0:
            return ""
        else:
            i = bisect.bisect(a, (timestamp, chr(127)))
            return a[i-1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)