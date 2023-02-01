# 352. Data Stream as Disjoint Intervals
# Union-Find

# https://leetcode.com/problems/data-stream-as-disjoint-intervals/solutions/297728/short-python-union-find-solution/
class UF:
    def __init__(self):
        self.p = {}
        self.intervals = {}

    def exists(self, x):
        return x in self.p
    
    def make_set(self, x):
        self.p[x] = x
        self.intervals[x] = [x, x]
    
    def find(self, x):
        if not self.exists(x):
            return None
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr is None or yr is None:
            return

        self.p[xr] = yr
        
        x_interval = self.intervals[xr]
        del self.intervals[xr]
        self.intervals[yr] = [min(self.intervals[yr][0], x_interval[0]), max(self.intervals[yr][1], x_interval[1])]

class SummaryRanges:

    def __init__(self):
        self.uf = UF()
        
    def addNum(self, value: int) -> None:
        if self.uf.exists(value):
            return
        self.uf.make_set(value)
        self.uf.union(value, value-1)
        self.uf.union(value, value+1)


    def getIntervals(self) -> List[List[int]]:
        return sorted(self.uf.intervals.values())
        

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
