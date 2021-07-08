# 715. Range Module
# Design / Binary Search

# https://leetcode.com/problems/range-module/discuss/169353/Ultra-concise-Python-(only-6-lines-of-actual-code)-(also-236ms-beats-100)
# runtime: O(n) for addRange and removeRange, since slice overwriting dominates binary search
# O(log n) for queryRange, since just binary search
class RangeModule:

    def __init__(self):
        self.arr = []

    def addRange(self, left: int, right: int) -> None:
        i = bisect_left(self.arr, left)
        j = bisect_right(self.arr, right)
        self.arr[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect_right(self.arr, left)
        j = bisect_left(self.arr, right)
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        i = bisect_left(self.arr, left)
        j = bisect_right(self.arr, right)
        self.arr[i:j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)